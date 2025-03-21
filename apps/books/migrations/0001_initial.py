# Generated by Django 5.1.6 on 2025-02-27 12:35

import apps.books.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("authors", models.CharField(max_length=255, verbose_name="Author(s)")),
                (
                    "isbn",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        unique=True,
                        verbose_name="ISBN",
                    ),
                ),
                (
                    "publisher",
                    models.CharField(max_length=100, verbose_name="Publisher"),
                ),
                (
                    "publication_year",
                    models.PositiveIntegerField(verbose_name="Publication Year"),
                ),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("fiction", "Fiction"),
                            ("non_fiction", "Non-Fiction"),
                            ("science", "Science"),
                            ("history", "History"),
                            ("literature", "Literature"),
                            ("other", "Other"),
                        ],
                        default="other",
                        max_length=20,
                        verbose_name="Genre",
                    ),
                ),
                ("language", models.CharField(max_length=50, verbose_name="Language")),
                (
                    "dewey_classification",
                    models.CharField(
                        blank=True,
                        max_length=10,
                        null=True,
                        verbose_name="Dewey Classification",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("available", "Available"),
                            ("borrowed", "Borrowed"),
                            ("under_repair", "Under Repair"),
                        ],
                        default="available",
                        max_length=20,
                        verbose_name="Status",
                    ),
                ),
                (
                    "physical_location",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Physical Location",
                    ),
                ),
                (
                    "copy_count",
                    models.PositiveIntegerField(default=1, verbose_name="Copy Count"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "cover_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=apps.books.models.book_cover_path,
                        verbose_name="Cover Image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Book",
                "verbose_name_plural": "Books",
            },
        ),
    ]
