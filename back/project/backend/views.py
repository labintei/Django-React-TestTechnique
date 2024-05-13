from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated





class CustomTokenObtainPairView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        token_obtain_pair_view = TokenObtainPairView.as_view()
        response = token_obtain_pair_view(request)
        if response.status_code == status.HTTP_200_OK:
            user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
            if user:
                refresh = RefreshToken.for_user(user)
                response.data['refresh'] = str(refresh)
                response.data['access'] = str(refresh.access_token)
        return response


class RegisterAPIView(APIView):
#     permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response = Response({
                'token': str(refresh.access_token),
                'user_id': user.id
            }, status=status.HTTP_201_CREATED)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        login = request.data.get('login')
        password = request.data.get('password')
        user = User.objects.filter(login=login, password=password).first()
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'token': str(refresh.access_token),
                'user_id': user.id
            }, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class ChatroomsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print("Chatrooms")
        print("Where are in Chatrooms")
        print(request)
        return Response({'message': 'Chatrooms list'}, status=status.HTTP_200_OK)

class OptionsAPIView(APIView):
    def options(self, request):
        allowed_methods = ['GET', 'POST']
        user = request.user  # Get the authenticated user
        user_data = {
            'username': user.username,
            'email': user.email,  # or any other user information you want to return
            # Add more user data fields as needed
        }
        return Response(user_data, status=status.HTTP_200_OK)