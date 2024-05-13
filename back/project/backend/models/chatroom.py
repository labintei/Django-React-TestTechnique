from django.db import models
from django.utils import timezone
# from .message import Message
# from .user import UserApp

class ChatRoom(models.Model):
    from .message import Message
    from .user import UserApp

    title = models.CharField(max_length=100)
    author = models.ForeignKey(UserApp, on_delete=models.CASCADE, related_name='created_chatrooms')
    users = models.ManyToManyField(UserApp, related_name='chatrooms')
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
