from django.db import models

def newspaper_cover_path(instance, filename):
    return f'newspapers/newspaper_{instance.id}/{filename}'

class Newspaper(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    publisher = models.CharField(max_length=100, verbose_name="Publisher")
    publication_date = models.DateField(verbose_name="Publication Date")
    language = models.CharField(max_length=50, verbose_name="Language")

    GENRE_CHOICES = [
        ('news', 'Noticias'),
        ('sports', 'Deportes'),
        ('technology', 'Tecnología'),
        ('entertainment', 'Entretenimiento'),
        ('other', 'Otro'),
    ]
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default='news', verbose_name="Genre")
    edition = models.CharField(max_length=100, blank=True, null=True, verbose_name="Edition")

    # Metadatos
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    cover_image = models.ImageField(upload_to=newspaper_cover_path, blank=True, null=True, verbose_name="Cover Image")

    # Disponibilidad y Ubicación
    STATUS_CHOICES = [
        ('available', 'Disponible'),
        ('borrowed', 'Prestado'),
        ('under_repair', 'En Reparación'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="Status")
    physical_location = models.CharField(max_length=100, blank=True, null=True, verbose_name="Physical Location")

    # Otros Atributos Opcionales
    issn = models.CharField(max_length=20, unique=True, blank=True, null=True, verbose_name="ISSN")
    pages = models.PositiveIntegerField(blank=True, null=True, verbose_name="Pages")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Price")

    def __str__(self):
        return f"{self.title} - {self.publication_date}"

    class Meta:
        verbose_name = "Newspaper"
        verbose_name_plural = "Newspapers"