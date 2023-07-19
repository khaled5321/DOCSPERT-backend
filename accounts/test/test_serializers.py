from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..serializers import UserSerializer


class UserSerializerTest(TestCase):
    def setUp(self):
        self.User = get_user_model()

    def test_serializer_not_valid(self):
        data = UserSerializer(
            data={
                "username": "test",
                "email": "test@gmail.com",
                "password": "very complicated password",
                "password2": "very complicated password 2",
            }
        )

        with self.assertRaisesMessage(
            serializers.ValidationError, "Passwords don't match"
        ):
            data.is_valid(raise_exception=True)

    def test_serializer_is_valid(self):
        data = UserSerializer(
            data={
                "username": "test",
                "email": "test@gmail.com",
                "password": "1ke[owke[oqwkqkd]]",
                "password2": "1ke[owke[oqwkqkd]]",
            }
        )

        self.assertTrue(data.is_valid(raise_exception=True))

    def test_serializer_create_method(self):
        data = UserSerializer(
            data={
                "username": "test",
                "email": "test@gmail.com",
                "password": "1ke[owke[oqwkqkd]]",
                "password2": "1ke[owke[oqwkqkd]]",
            }
        )

        data.is_valid(raise_exception=True)

        data = data.create(validated_data=data.validated_data)

        user = self.User.objects.get(username="test")

        self.assertEqual(data, user)
