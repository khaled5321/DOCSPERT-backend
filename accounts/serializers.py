from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "password2", "is_author")
        read_only_fields = ("id",)

    def validate(self, data):
        """
        Check that the two password fields match.
        """
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords don't match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            is_author=validated_data["is_author"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user
