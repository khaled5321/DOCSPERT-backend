from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from books.models import Book
from .permissions import AuthorPermission, ReaderPermission


# permession testing.
class PermissionsTest(TestCase):
    def setUp(self):
        self.User = get_user_model()

        self.author_user = self.User.objects.create(
            username="author", email="author@gmail.com", is_author=True
        )
        self.reader_user = self.User.objects.create(
            username="reader", email="reader@gmail.com", is_author=False
        )
        self.another_author = self.User.objects.create(
            username="another author", email="author2@gmail.com", is_author=True
        )

        self.book = Book.objects.create(author=self.another_author, title="test")

        self.factory = RequestFactory()

    def test_author_user_return_true_on_post(self):
        request = self.factory.post(
            "/api/v1/books/", data={"author": self.author_user.id, "title": "book"}
        )
        request.user = self.author_user

        permission_check = AuthorPermission()

        permission = permission_check.has_permission(request, None)

        self.assertTrue(permission)

    def test_non_author_user_returns_false_on_post(self):
        request = self.factory.post(
            "/api/v1/books/", data={"author": self.reader_user.id, "title": "book"}
        )
        request.user = self.reader_user

        permission_check = ReaderPermission()

        permission = permission_check.has_permission(request, None)

        self.assertFalse(permission)

    def test_reader_user_returns_true_on_safe_method(self):
        request = self.factory.get("/api/v1/books/")
        request.user = self.reader_user

        permission_check = ReaderPermission()

        permission = permission_check.has_permission(request, None)

        self.assertTrue(permission)

    def test_only_book_author_can_edit_his_book(self):
        request = self.factory.delete(f"/api/v1/books/{self.book.id}/")
        request.user = self.author_user

        permission_check = AuthorPermission()

        permission = permission_check.has_object_permission(request, None, self.book)

        self.assertFalse(permission)
