from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserLoginAPIView,
    UserProfileAPIView,
    UserRegistrationAPIView,
    UserViewSet,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('profile/<int:pk>/', UserProfileAPIView.as_view(), name='user-profile'),
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
]
