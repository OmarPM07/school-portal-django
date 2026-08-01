from django.shortcuts import render, get_object_or_404
from .models import PaginaInstitucional

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def pagina_institucional(request, slug):
    pagina = get_object_or_404(PaginaInstitucional, slug=slug, activo=True)
    return render(request, 'core/pagina_institucional.html', {'pagina': pagina})