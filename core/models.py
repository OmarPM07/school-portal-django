from django.db import models

# Create your models here.

class PaginaInstitucional(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(
        unique=True,
        help_text="Identificador único usado en la URL (ej: historia, mision, vision)"
    )
    imagen = models.ImageField(upload_to='institucional/')
    contenido = models.TextField()
    orden = models.PositiveIntegerField(
        default=0,
        help_text="Orden de aparición en el menú (menor número aparece primero)"
    )
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['orden']
        verbose_name = "Página institucional"
        verbose_name_plural = "Páginas institucionales"

    def __str__(self):
        return self.titulo