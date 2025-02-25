from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Roles disponibles
    ROL_CHOICES = [
        ('empleado', 'Empleado'),
        ('administrador', 'Administrador'),
        ('jefe_turno', 'Jefe de Turno'),
    ]

    # Campos adicionales
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='empleado')
    numero_empleado = models.CharField(max_length=20, blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"