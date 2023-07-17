from django.urls import path
from .views import *

urlpatterns = [
    path("auth/signup/", UserSignUp.as_view(), name="signup"),
    path("users/currentuser/", GetUser.as_view(), name="get_user"),
]
