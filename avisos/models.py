# avisos/models.py

from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from taggit.managers import TaggableManager


class Aviso(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=220)
    imagen = models.ImageField(upload_to='avisos/%Y/%m/')
    resumen = models.CharField(
        max_length=250,
        help_text="Descripción corta para la tarjeta en la lista de avisos"
    )
    contenido = CKEditor5Field('Contenido', config_name='extends')
    publicado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    tags = TaggableManager()

    class Meta:
        ordering = ['-publicado']
        verbose_name = "Aviso"
        verbose_name_plural = "Avisos"

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('avisos:detalle', args=[self.slug])