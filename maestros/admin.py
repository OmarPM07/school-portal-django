from django.contrib import admin
from .models import Maestro

# Register your models here.

@admin.register(Maestro)
class MaestroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especialidad', 'carrera', 'activo', 'orden')
    list_filter = ('activo', 'carrera')
    search_fields = ('nombre', 'especialidad')
    ordering = ('orden', 'nombre')
