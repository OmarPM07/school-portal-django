# avisos/urls.py

from django.urls import path
from . import views

app_name = 'avisos'

urlpatterns = [
    path('', views.lista_avisos, name='lista'),
    path('tag/<slug:tag_slug>/', views.lista_avisos, name='lista_por_tag'),
    path('<slug:slug>/', views.detalle_aviso, name='detalle'),
]