from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=150)
    slug = models.SlugField(
        unique=True,
        help_text="Identificador único para la URL (ej: produccion-agropecuaria)"
    )
    imagen_principal = models.ImageField(
        upload_to='carreras/principal/',
        help_text="Imagen destacada que se muestra en la tarjeta de la carrera"
    )
    resumen = models.CharField(
        max_length=250,
        help_text="Descripción corta para la tarjeta en la lista de oferta educativa"
    )
    descripcion = CKEditor5Field('Descripción Carrera', config_name='extends')
    perfil_egreso = CKEditor5Field('Perfil Egreso', config_name='extends', blank=True, null=True)
    campo_laboral = CKEditor5Field('Campo Laboral', config_name='extends', blank=True, null=True)
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['orden']
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"
    
    def __str__(self):
        return self.nombre

class ImagenCarrera(models.Model):
    carrera = models.ForeignKey(
        Carrera,
        related_name='imagenes',
        on_delete=models.CASCADE
    )
    imagen = models.ImageField(upload_to='carreras/galeria/')
    descripcion = models.CharField(
        max_length=150,
        blank=True,
        help_text="Texto alternativo o pie de foto (opcional)"
    )
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name = "Imagen de carrera"
        verbose_name_plural = "Imágenes de carrera"

    def __str__(self):
        return f"Imagen de {self.carrera.nombre}"