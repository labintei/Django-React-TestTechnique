from rest_framework import serializers
from .models import User, ChatRoom, Message
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid username or password")

        if not user.check_password(data['password']):
            raise serializers.ValidationError("Invalid username or password")

        return user

class ChatRoomSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault())

    class Meta:
        model = ChatRoom
        fields = ['id', 'title', 'author', 'users']

    def create(self, validated_data):
        author = validated_data['author']
        title = validated_data['title']
        chatroom = ChatRoom.create_chatroom(title=title, author=author)
        return chatroom
    

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'author', 'chatroom', 'content', 'publication_date']