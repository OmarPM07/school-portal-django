from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('conocenos/<slug:slug>', views.pagina_institucional, name='pagina_institucional'),
]