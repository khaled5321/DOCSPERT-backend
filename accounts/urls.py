from django.urls import path
from .views import *

urlpatterns = [
    path("auth/signup/", UserSignUp.as_view(), name="signup"),
    path("users/currentuser/", GetCurrentUser.as_view(), name="get_current_user"),
]
