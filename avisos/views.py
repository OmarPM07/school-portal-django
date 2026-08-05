# avisos/views.py

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from .models import Aviso


def lista_avisos(request, tag_slug=None):
    avisos = Aviso.objects.filter(activo=True)
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        avisos = avisos.filter(tags__in=[tag])

    paginator = Paginator(avisos, 6)
    page_number = request.GET.get('page', 1)

    try:
        avisos_pagina = paginator.page(page_number)
    except PageNotAnInteger:
        avisos_pagina = paginator.page(1)
    except EmptyPage:
        avisos_pagina = paginator.page(paginator.num_pages)

    return render(request, 'avisos/lista.html', {
        'avisos': avisos_pagina,
        'tag': tag,
    })


def detalle_aviso(request, slug):
    aviso = get_object_or_404(Aviso, slug=slug, activo=True)
    return render(request, 'avisos/detalle.html', {'aviso': aviso})