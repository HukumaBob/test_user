from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User


class UserAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')

    def test_user_registration(self):
        # Ensure we can register a new user with unique credentials
        url = reverse('user-registration')
        data = {'username': 'newuser', 'email': 'new@example.com', 'password': 'newpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        # Ensure we can log in with valid credentials
        url = reverse('user-login')
        data = {'username': 'testuser', 'password': 'testpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_duplicate_username_registration(self):
        # Ensure duplicate username registration fails
        url = reverse('user-registration')
        data = {'username': 'testuser', 'email': 'duplicate@example.com', 'password': 'testpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_email_registration(self):
        # Ensure duplicate email registration fails
        url = reverse('user-registration')
        data = {'username': 'duplicateuser', 'email': 'test@example.com', 'password': 'testpass'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
