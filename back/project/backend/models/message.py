from django.db import models
from django.utils import timezone
# from .user import UserApp

class Message(models.Model):
    from .user import UserApp
    author = models.ForeignKey(UserApp, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_message(cls, author, content):
        message = cls(author=author, content=content, publication_date=timezone.now())
        message.save()
        return message