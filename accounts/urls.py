from django.urls import path
from .views import *

urlpatterns = [
    path("users/signup/", UserSignUp.as_view(), name="signup"),
    path("users/<int:id>/", GetUser.as_view(), name="get_user"),
]
