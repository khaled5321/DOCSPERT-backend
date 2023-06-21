from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    email = models.EmailField(
        unique=True, null=False, blank=False, validators=[EmailValidator]
    )

    is_author = models.BooleanField(default=False)

    def __str__(self):
        return self.username
