from rest_framework import serializers
from .models import User, ChatRoom, Message
# from .models.user import UserApp
# from .models.chatroom import ChatRoom
# from .models.message import Message



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'login', 'password']

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user
    
    
class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'title', 'author', 'messages', 'users']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'author', 'chatroom', 'content', 'publication_date']