from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import PermissionDenied
from accounts.permissions import AuthorPermission, ReaderPermission
from .serializers import BookSerializer, PageSerializer
from .models import Book, Page


class BookListCreateAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by("created_at")
    permission_classes = [ReaderPermission | AuthorPermission]


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "id"
    permission_classes = [ReaderPermission | AuthorPermission]


class PageListCreateAPIView(ListCreateAPIView):
    serializer_class = PageSerializer
    permission_classes = [ReaderPermission | AuthorPermission]

    def get_queryset(self):
        pages = Page.objects.filter(book=self.kwargs["id"]).order_by("number")
        return pages


class PageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PageSerializer
    lookup_field = "id"
    permission_classes = [ReaderPermission | AuthorPermission]

    def get_queryset(self):
        pages = Page.objects.filter(book=self.kwargs["book_id"])
        return pages
