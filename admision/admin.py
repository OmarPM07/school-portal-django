from django.contrib import admin
from .models import ConvocatoriaAdmision, FichaInscripcion

# Register your models here.

class FichaInscripcionInline(admin.TabularInline):
    model = FichaInscripcion
    extra = 1
    fields = ('semestre', 'archivo', 'orden')

@admin.register(ConvocatoriaAdmision)
class ConvocatoriaAdmisionAdmin(admin.ModelAdmin):
    list_display = ('ciclo_escolar', 'fecha_inicio_registro', 'fecha_fin_registro', 'activo', 'actualizado')
    list_filter = ('activo',)
    search_fields = ('ciclo_escolar',)
    ordering = ('-fecha_inicio_registro',)
    inlines = [FichaInscripcionInline]