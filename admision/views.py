from django.shortcuts import render
from django.http import Http404
from .models import ConvocatoriaAdmision

# Create your views here.

def admision(request):
    convocatoria = ConvocatoriaAdmision.objects.filter(activo=True).first()
    if not convocatoria:
        raise Http404("No hay una convocatoria de admisión para este momento.")
    return render(
        request,
        'admision/admision.html',
        {'convocatoria': convocatoria}
    )