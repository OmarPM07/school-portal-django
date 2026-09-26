from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class InformacionAlumnos(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(
        unique=True,
        help_text="Identificador único para la URL (ej: becas, tramites, horarios)"
    )
    contenido = CKEditor5Field('Contenido', config_name='extends')
    archivo_adjunto = models.FileField(
        upload_to='alumnos/documentos',
        blank=True,
        null=True,
        help_text="Opcional: documento descargable relacionado"
    )
    orden = models.PositiveIntegerField(default=0)
    activo = models.BooleanField(default=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['orden']
        verbose_name = "Información para alumno"
        verbose_name_plural = "Información para alumnos"
    
    def __str__(self):
        return self.titulo

class Actividad(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=170)
    imagen_principal = models.ImageField(upload_to='alumnos/actividades/principal/')
    resumen = models.CharField(max_length=250)
    descripcion = CKEditor5Field('Descripcion', config_name='extends', blank=True)
    fecha = models.DateField()
    activo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-fecha']
        verbose_name = "Actividad"
        verbose_name_plural = "Actividades"
    
    def __str__(self):
        return self.titulo

class ImagenActividad(models.Model):
    actividad =models.ForeignKey(
        Actividad,
        related_name='imagenes',
        on_delete=models.CASCADE
    )
    imagen = models.ImageField(upload_to='alumnos/actividades/galeria/')
    descripcion = models.CharField(max_length=150, blank=True)
    orden = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['orden']
        verbose_name = "Imagen de actividad"
        verbose_name_plural = "Imagenes de actividad"

    def __str__(self):
        return f"Imagen de {self.actividad.titulo}"