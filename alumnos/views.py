from django.shortcuts import render, get_object_or_404
from .models import Actividad, InformacionAlumnos

# Create your views here.

def lista_informacion(request):
    secciones = InformacionAlumnos.objects.filter(activo=True)
    return render(
        request,
        'alumnos/informacion.html', 
        {'secciones': secciones}
    )

def detalle_informacion(request, slug):
    seccion = get_object_or_404(InformacionAlumnos, slug=slug, activo=True)
    return render(
        request,
        'alumnos/detalle_informacion.html',
        {'seccion': seccion}
    )

def lista_actividades(request):
    actividades = Actividad.objects.filter(activo=True)
    return render(
        request,
        'alumnos/actividades.html',
        {'actividades': actividades}
    )

def detalle_actividad(request, slug):
    actividad = get_object_or_404(Actividad, slug=slug, activo=True)
    return render(
        request,
        'alumnos/detalle_actividad.html',
        {'actividad': actividad}
    )