from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

class User(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    chatrooms = models.ManyToManyField('ChatRoom', related_name='memberships')  # Changed related_name

    def __str__(self):
        return self.login

    def check_password(self, password):
        return self.password == password

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create_message(cls, author, content):
        message = cls(author=author, content=content, publication_date=timezone.now())
        message.save()
        return message

class ChatRoom(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_chatrooms')
    users = models.ManyToManyField(User, related_name='bis')
    messages = models.ManyToManyField(Message, related_name='chatroom_messages')

    @classmethod
    def create_chatroom(cls, title, author):
        chatroom = cls.objects.create(title=title, author=author)
        chatroom.users.add(author)
        return chatroom

    def add_message(self, author, content):
        message = Message.create_message(author, content)
        self.messages.add(message)
        return message

    def get_messages(self):
        return list(self.messages.all()) if self.messages.exists() else []

