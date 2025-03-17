import os
import shutil
from django.db import models
from django.conf import settings

def newspaper_cover_path(instance, filename):
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

    copete = models.CharField(
        max_length=255,  # Ajusta la longitud según tus necesidades
        blank=True,
        null=True,
        verbose_name="Copete"
    )

    def __str__(self):
        return f"{self.title} - {self.get_scope_display()} ({self.publication_date})"

    class Meta:
        verbose_name = "Newspaper"
        verbose_name_plural = "Newspapers"

    def save(self, *args, **kwargs):
        """ Sobrescribe el método save para mover la imagen a la carpeta definitiva después de guardar """
        super().save(*args, **kwargs)  # Guarda el objeto primero para obtener un ID

        if self.cover_image and 'temp' in self.cover_image.name:
            old_file_path = os.path.join(settings.MEDIA_ROOT, self.cover_image.name)
            new_dir = os.path.join(settings.MEDIA_ROOT, f'newspapers/newspaper_{self.id}')
            new_filename = os.path.basename(self.cover_image.name)
            new_file_path = os.path.join(new_dir, new_filename)

            # Asegurar que el directorio de destino existe
            os.makedirs(new_dir, exist_ok=True)

            # Mover el archivo si existe
            if os.path.exists(old_file_path):
                shutil.move(old_file_path, new_file_path)
                self.cover_image.name = f'newspapers/newspaper_{self.id}/{new_filename}'
                super().save(update_fields=['cover_image'])  # Guarda nuevamente solo el campo cover_image
            
            # Intentar eliminar el directorio temporal si está vacío
            temp_dir = os.path.dirname(old_file_path)
            try:
                if os.path.exists(temp_dir) and not os.listdir(temp_dir):
                    os.rmdir(temp_dir)
            except OSError:
                pass
