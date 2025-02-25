from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ('username', 'email', 'rol', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('rol', 'numero_empleado', 'fecha_ingreso')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información adicional', {'fields': ('rol', 'numero_empleado', 'fecha_ingreso')}),
    )

admin.site.register(Usuario, UsuarioAdmin)