from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer, PageSerializer
from .models import Book, Page


class BookListCreateAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "id"


class PageListCreateAPIView(ListCreateAPIView):
    serializer_class = PageSerializer

    def get_queryset(self):
        pages = Page.objects.filter(book=self.kwargs["book"])
        return pages


class PageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PageSerializer
    lookup_field = "id"

    def get_queryset(self):
        pages = Page.objects.filter(book=self.kwargs["book_id"])
        return pages
