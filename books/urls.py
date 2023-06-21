from django.urls import path
from .views import *

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view(), name="book_list_create"),
    path(
        "books/<int:id>/",
        BookRetrieveUpdateDestroyAPIView.as_view(),
        name="book_get_update_delete",
    ),
    path(
        "books/<int:id>/pages/",
        PageListCreateAPIView.as_view(),
        name="page_list_create",
    ),
    path(
        "books/<int:book_id>/pages/<int:id>/",
        PageRetrieveUpdateDestroyAPIView.as_view(),
        name="page_get_update_delete",
    ),
]
