# from django.urls import path
# from .views import register, CustomTokenObtainPairView, login, chatrooms, options_view


# urlpatterns = [
#     path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('register/', register, name='register'),
#     path('login/', login, name='login'),
#     path('chatrooms/', chatrooms , name='chatrooms'),
#     path('options/', options_view , name='options'),
# ]

from django.urls import path
from .views import CustomTokenObtainPairView, RegisterAPIView, LoginAPIView, ChatroomsAPIView, OptionsAPIView 

urlpatterns = [
    #Authentication
    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('chatrooms/', ChatroomsAPIView.as_view(), name='chatrooms'),
    path('options/', OptionsAPIView.as_view(), name='options'),
]
