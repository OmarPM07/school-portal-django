# avisos/admin.py

from django.contrib import admin
from .models import Aviso


@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicado', 'activo')
    list_filter = ('activo', 'tags', 'publicado')
    search_fields = ('titulo', 'resumen', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'publicado'
    ordering = ('-publicado',)