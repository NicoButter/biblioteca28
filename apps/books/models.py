from django.db import models

def book_cover_path(instance, filename):
    return f'books/book_{instance.id}/{filename}'

class Book(models.Model):
    # General Information
    title = models.CharField(max_length=255, verbose_name="Title")
    authors = models.CharField(max_length=255, verbose_name="Author(s)")
    isbn = models.CharField(max_length=20, unique=True, verbose_name="ISBN", blank=True, null=True)
    publisher = models.CharField(max_length=100, verbose_name="Publisher")
    publication_year = models.PositiveIntegerField(verbose_name="Publication Year")

    # Classification and Categorization
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('literature', 'Literature'),
        ('other', 'Other'),
    ]
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='other', verbose_name="Genre")
    language = models.CharField(max_length=50, verbose_name="Language")
    dewey_classification = models.CharField(max_length=10, verbose_name="Dewey Classification", blank=True, null=True)

    # Status and Availability
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('under_repair', 'Under Repair'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="Status")
    physical_location = models.CharField(max_length=100, verbose_name="Physical Location", blank=True, null=True)
    copy_count = models.PositiveIntegerField(default=1, verbose_name="Copy Count")

    # Additional Metadata
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    cover_image = models.ImageField(upload_to=book_cover_path, blank=True, null=True, verbose_name="Cover Image")

    def __str__(self):
        return f"{self.title} - {self.authors}"

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"