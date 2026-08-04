from django.contrib import admin
from .models import Carrera, ImagenCarrera

# Register your models here.

class ImagenCarreraInline(admin.TabularInline):
    model = ImagenCarrera
    extra = 1
    fields = ('imagen', 'descripcion', 'orden')

@admin.register(Carrera)
class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'orden', 'activo', 'actualizado')
    list_filter = ('activo',)
    search_fields = ('nombre', 'resumen', 'descripcion')
    prepopulated_fields = {'slug': ('nombre',)}
    ordering = ('orden',)
    inlines = [ImagenCarreraInline]