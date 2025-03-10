import os
from django.db import models
from django.conf import settings  # Importa settings para acceder a MEDIA_ROOT

def newspaper_cover_path(instance, filename):
    # Usa 'temp' si el ID no existe, o el ID real si ya está guardado
    if instance.id:
        return f'newspapers/newspaper_{instance.id}/{filename}'
    else:
        return f'newspapers/temp/{filename}'

class Newspaper(models.Model):
    STATUS_CHOICES = [
        ('available', 'Disponible'),
        ('borrowed', 'Prestado'),
        ('under_repair', 'En Reparación'),
    ]

    SCOPE_CHOICES = [
        ('nacional', 'Nacional'),
        ('provincial', 'Provincial'),
        ('regional', 'Regional'),
    ]
    scope = models.CharField(
        max_length=20,
        choices=SCOPE_CHOICES,
        default='nacional',
        verbose_name="Alcance"
    )

    title = models.CharField(max_length=255, verbose_name="Title")
    publisher = models.CharField(max_length=100, verbose_name="Publisher")
    publication_date = models.DateField(verbose_name="Publication Date")
    language = models.CharField(max_length=50, verbose_name="Language")

    GENRE_CHOICES = [
        ('noticias', 'Noticias'),
        ('deportes', 'Deportes'),
        ('tecnologia', 'Tecnología'),
        ('entretenimiento', 'Entretenimiento'),
        ('politica', 'Política'),
        ('cultura', 'Cultura'),
        ('otros', 'Otros'),
    ]
    genre = models.CharField(
        max_length=20,
        choices=GENRE_CHOICES,
        default='noticias',
        verbose_name="Género"
    )

    edition = models.CharField(max_length=100, blank=True, null=True, verbose_name="Edition")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    cover_image = models.ImageField(upload_to=newspaper_cover_path, blank=True, null=True, verbose_name="Cover Image")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available',
        verbose_name="Status"
    )
    physical_location = models.CharField(max_length=100, blank=True, null=True, verbose_name="Physical Location")
    issn = models.CharField(max_length=20, unique=True, blank=True, null=True, verbose_name="ISSN")
    pages = models.PositiveIntegerField(blank=True, null=True, verbose_name="Pages")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Price")

    def __str__(self):
        return f"{self.title} - {self.get_scope_display()} ({self.publication_date})"

    class Meta:
        verbose_name = "Newspaper"
        verbose_name_plural = "Newspapers"

    def save(self, *args, **kwargs):
        # Primero guarda el periódico para obtener un ID
        super().save(*args, **kwargs)
        
        if self.cover_image and 'temp' in self.cover_image.path:
            # Define la nueva ruta con el ID real
            new_dir = f'newspapers/newspaper_{self.id}'
            new_filename = os.path.basename(self.cover_image.name)  # Nombre original del archivo
            new_path = os.path.join(new_dir, new_filename)
            
            # Crea el directorio si no existe
            os.makedirs(os.path.join(settings.MEDIA_ROOT, new_dir), exist_ok=True)
            
            # Obtiene la ruta antigua y nueva
            old_file_path = self.cover_image.path
            new_file_path = os.path.join(settings.MEDIA_ROOT, new_path)
            
            # Mueve el archivo
            os.rename(old_file_path, new_file_path)
            
            # Actualiza el campo cover_image con la nueva ruta
            self.cover_image.name = new_path
            super().save(update_fields=['cover_image'])  # Guarda solo el campo modificado
            
            # Elimina el directorio temporal si está vacío
            try:
                temp_dir = os.path.dirname(old_file_path)
                if not os.listdir(temp_dir):
                    os.rmdir(temp_dir)
            except OSError:
                pass
