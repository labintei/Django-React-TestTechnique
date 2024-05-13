from django.contrib import admin
from .models import User, ChatRoom, Message
# from .models.user import UserApp
# from .models.chatroom import ChatRoom
# from .models.message import Message

admin.site.register(Message)
admin.site.register(User)
admin.site.register(ChatRoom)
