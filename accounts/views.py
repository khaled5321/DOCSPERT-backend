from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import UserSerializer
from .models import User


class UserSignUp(CreateAPIView):
    serializer_class = UserSerializer


class GetUser(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"
