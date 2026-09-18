from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from carreras.models import Carrera

# Create your models here.

class Maestro(models.Model):
    nombre = models.CharField(max_length=150)
    foto = models.ImageField(upload_to='maestros/')
    especialidad = models.CharField(max_length=150, help_text="Asignatura o módulo profesional que imparte")
    carrera = models.ForeignKey(
        Carrera, 
        related_name='maestros',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Opcional: carrera a la esta asociado principalmente")
    semblanza = CKEditor5Field(
        'Semblanza',
        config_name = 'extends',
        blank = True,
        help_text = "Breve reseña profesional (opcional)"
    )
    correo = models.EmailField(blank=True),
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name = "Maestro"
        verbose_name_plural = "Maestros"

    def __str__(self):
        return self.nombre