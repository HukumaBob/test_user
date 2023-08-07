from django.urls import path, include
from .views import (
    UserLoginAPIView,
    UserRegistrationAPIView,
)

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
]
