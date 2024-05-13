from django.urls import path
from .views import UserRegistrationView, UserLoginView, ChatRoomCreateView

urlpatterns = [
    path('chatrooms/', ChatRoomCreateView.as_view(), name='create_chatroom'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]