from django.urls import path
from . import views

app_name = 'alumnos'

urlpatterns = [
    path('', views.lista_informacion, name='informacion'),
    path('info/<slug:slug>/', views.detalle_informacion, name='detalle_informacion'),
    path('actividades/', views.lista_actividades, name='actividades'),
    path('actividades/<slug:slug>/', views.detalle_actividad, name='detalle_actividad'),
]