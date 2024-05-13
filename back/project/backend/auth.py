# from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
# from models import User

from .models.user import User
# User = get_user_model()

class CustomAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(login=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        return None