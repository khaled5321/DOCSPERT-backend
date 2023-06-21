from rest_framework.serializers import ModelSerializer
from .models import Book, Page


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        read_only = ("created_at", "updated_at")


class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"
        read_only = ("created_at", "updated_at")
