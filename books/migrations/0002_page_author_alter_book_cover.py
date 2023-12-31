# Generated by Django 4.2.2 on 2023-06-22 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author_pages",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="cover",
            field=models.ImageField(
                blank=True, default="books/default.jpg", null=True, upload_to="books/"
            ),
        ),
    ]
