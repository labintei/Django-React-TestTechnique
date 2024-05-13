from django.db import models
from django.utils import timezone
# from .chatroom import ChatRoom

class UserApp(models.Model):
    from .chatroom import ChatRoom
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    chatrooms = models.ManyToManyField(ChatRoom, related_name='users_available')  # Changed related_name

    def __str__(self):
        return self.login

    def check_password(self, password):
        return self.password == password
