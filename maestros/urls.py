from django.urls import path
from . import views

app_name = 'maestros'

urlpatterns = [
    path('', views.lista_maestros, name='lista')

]