from django.db import models
from apps.newspaper.models import Newspaper

def cardex_file_path(instance, filename):
    return f'cardex/cardex_{instance.id}/{filename}'

class Cardex(models.Model):
    newspaper = models.ForeignKey(
        Newspaper,
        on_delete=models.CASCADE,
        related_name='cardex_entries',
        verbose_name="Periódico"
    )
    circulation = models.PositiveIntegerField(verbose_name="Circulación")
    issue_number = models.CharField(max_length=50, verbose_name="Número de Edición")
    content_summary = models.TextField(verbose_name="Resumen de Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    file = models.FileField(upload_to=cardex_file_path, blank=True, null=True)

    def __str__(self):
        return f"Ficha Cardex - {self.newspaper.title} (Edición: {self.issue_number})"

    class Meta:
        verbose_name = "Ficha Cardex"
        verbose_name_plural = "Fichas Cardex"