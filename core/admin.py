from django.contrib import admin
from .models import PaginaInstitucional

# Register your models here.

@admin.register(PaginaInstitucional)
class PaginaInstitucionalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'orden', 'activo', 'actualizado')
    list_filter = ('activo',)
    search_fields = ('titulo', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ('orden',)