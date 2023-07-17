from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


class UserSignUp(CreateAPIView):
    serializer_class = UserSerializer


class GetUser(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        """
        Return current user.
        """
        current_user = User.objects.get(id=request.user.id)
        current_user = UserSerializer(current_user).data
        
        return Response(current_user)
