from django.shortcuts import render
from .models import Maestro

# Create your views here.

def lista_maestros(request):
    maestros = Maestro.objects.filter(activo=True)
    return render(request, 'maestros/lista.html', {'maestros': maestros})
