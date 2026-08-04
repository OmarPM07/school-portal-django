from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class ConvocatoriaAdmision(models.Model):
    ciclo_escolar = models.CharField(max_length=20, help_text="Ej: 2026-2027")
    contenido = CKEditor5Field(
        'Contenido', 
        config_name='extends', 
        help_text="Descripción general: proceso de registro, examen diagnóstico y resultados",
        blank=True,
        null=True
    )
    fecha_inicio_registro = models.DateField()
    fecha_fin_registro = models.DateField()
    fecha_examen_diagnostico = models.DateField()
    fecha_publicacion_resultados = models.DateField()
    fecha_inicio_propedeutico = models.DateField()
    
    convocatoria_pdf = models.FileField(
        upload_to='admision/formatos/',
        help_text="Documentos de convocatoria PDF"
    )
    formato_solicitud_pdf = models.FileField(
        upload_to='admision/formatos/',
        help_text="Formato de solicitud de ingreso en PDF"
    )

    activo = models.BooleanField(
        default=False,
        help_text="Marca solo una convocatoria como activa; será la que se muestre en el sitio"
    )
    
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha_inicio_registro']
        verbose_name = "Convocatoria de admisión"
        verbose_name_plural = "Convocatorias de admisión"

    def __str__(self):
        return f"Convocatoria {self.ciclo_escolar}"
    
    def save(self, *args, **kwargs):
        if self.activo:
            ConvocatoriaAdmision.objects.exclude(pk=self.pk).update(activo=False)
        super().save(*args, **kwargs)

class FichaInscripcion(models.Model):
    convocatoria = models.ForeignKey(
        ConvocatoriaAdmision,
        related_name='fichas_inscripcion',
        on_delete=models.CASCADE
    )
    semestre = models.CharField(
        max_length=50,
        help_text="Ej: 1er semestre, 3er semestre, 5to semestre"
    )
    archivo = models.FileField(upload_to='admision/fichas/')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden']
        verbose_name = "Ficha de inscripción"
        verbose_name_plural = "Fichas de inscripción"

    def __str__(self):
        return f"Ficha {self.semestre} - {self.convocatoria.ciclo_escolar}"
    