from django.contrib.auth.hashers import make_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationAPIView(APIView):
    """
    API view for user registration.

    Allows new users to register by providing necessary information.

    HTTP Methods:
    - POST: Register a new user.

    Permissions:
    - AllowAny: Anyone can access this view.
    """

    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Securely hash the password before saving the user
            password = make_password(serializer.validated_data['password'])
            serializer.validated_data['password'] = password

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
    """
    API view for user login.

    Allows users to authenticate and obtain JWT tokens for accessing protected endpoints.

    HTTP Methods:
    - POST: Authenticate user and provide JWT tokens.

    Permissions:
    - AllowAny: Anyone can access this view.
    """

    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        """
        Authenticate the user and provide JWT tokens upon successful login.

        Args:
        - request: The HTTP request object containing user credentials.

        Returns:
        - Response: A response containing JWT tokens and user data upon successful login.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'message': 'Please provide both username and password.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        from django.contrib.auth import authenticate
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }

        return Response(response_data, status=status.HTTP_200_OK)



