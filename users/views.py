from rest_framework import generics, permissions
from users.models import CustomUser
from users.serializers import CustomUserSerializer,UserSerializer
from django.contrib.auth import get_user_model
import logging
logger=logging.getLogger(__name__)

class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

User=get_user_model()

class UserProfileView(generics.RetrieveAPIView):
    """
    API endpoints to fetch the authenticated user's profile.
    """
    serializer_class=UserSerializer
    # permission_classes = [permissions.AllowAny]
    permission_classes=[permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        print(user)
        logger.info(f"Authenticated user: {user}")
        return user
    
