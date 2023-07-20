from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()


class UserSignUpViewTest(APITestCase):
    def setUp(self):
        self.url = reverse_lazy("signup")

    def test_post_request(self):
        # Test a POST request to the view
        response = self.client.post(
            self.url,
            {
                "username": "testuser",
                "email": "testuser@example.com",
                "password": "verycomplicatedpassword",
                "password2": "verycomplicatedpassword",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testuser")


class GetCurrentUserViewTest(APITestCase):
    def setUp(self):
        self.url = reverse_lazy("get_current_user")
        self.current_user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="verycomplicatedpassword",
        )

    def test_get_current_user(self):
        self.assertTrue(
            self.client.login(username="testuser", password="verycomplicatedpassword")
        )

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "testuser")
        self.assertEqual(response.data["id"], self.current_user.id)

    def test_user_must_be_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
