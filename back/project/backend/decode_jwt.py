from django.core.management.base import BaseCommand
from django.conf import settings
import jwt

class Command(BaseCommand):
    help = 'Decode a JWT token'

    def add_arguments(self, parser):
        parser.add_argument('token', type=str, help='The JWT token to decode')

    def handle(self, *args, **kwargs):
        token = kwargs['token']
        try:
            decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            self.stdout.write(self.style.SUCCESS(f'Decoded Token: {decoded}'))
        except jwt.ExpiredSignatureError:
            self.stdout.write(self.style.ERROR('Token has expired'))
        except jwt.InvalidTokenError:
            self.stdout.write(self.style.ERROR('Invalid token'))