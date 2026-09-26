from django.contrib import admin
from .models import Actividad, ImagenActividad, InformacionAlumnos

# Register your models here.

@admin.register(InformacionAlumnos)
class InformacionAlumnosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'orden', 'activo', 'actualizado')
    list_filter = ('activo',)
    search_fields = ('titulo', 'contenido')
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ('orden',)

class ImagenActividadInline(admin.TabularInline):
    model = ImagenActividad
    extra = 1
    fields = ('imagen', 'descripcion', 'orden')

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'activo')
    list_filter = ('activo',)
    search_fields = ('titulo', 'resumen')
    prepopulated_fields = {'slug': ('titulo',)}
    ordering = ('-fecha',)
    inlines = [ImagenActividadInline]