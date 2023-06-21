from django.db import models
from accounts.models import User


# Create your models here.
class Book(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to="books/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="pages")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_pages"
    )
    number = models.IntegerField()
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
