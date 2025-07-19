from django.urls import path
from .views import *

urlpatterns = [
    # Ruta para la vista de inicio
    path('', inicio, name='inicio'),
    path('agregar-consolas/', agregar_consolas, name='agregar-consolas'),
    path('agregar-juegos/', agregar_juegos, name='agregar-juegos'),
    path('agregar-accesorios/', agregar_accesorios, name='agregar-accesorios'),
]