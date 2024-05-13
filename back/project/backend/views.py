import jwt
from datetime import datetime, timedelta
from django.conf import settings
from rest_framework import generics, status
from .models import User
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, ChatRoom
from .serializers import UserSerializer, UserLoginSerializer, ChatRoomSerializer
from rest_framework.permissions import IsAuthenticated

from datetime import datetime, timedelta, timezone

def generate_jwt(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.now(timezone.utc) + timedelta(minutes=60),  # Corrected
        'iat': datetime.now(timezone.utc)  # Corrected
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.create(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            access_token = generate_jwt(user)
            return Response({
                'user': serializer.data,
                'access': access_token,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data  # Since validate returns user, it's stored here
            access_token = generate_jwt(user)
            return Response({
                'user': UserSerializer(user).data,  # Serialize user data securely
                'access': access_token,
            }, status=status.HTTP_200_OK)
        else:
            return Response("Invalid username or password", status=status.HTTP_404_NOT_FOUND)


class ChatRoomCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print("Authorization Header:", request.headers.get('Authorization', 'No header found'))
        print("Handling POST request.")
        return Response("Hey", status=status.HTTP_201_CREATED)
