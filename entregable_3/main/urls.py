from django.urls import path
from .views import *

urlpatterns = [
    # Ruta para la vista de inicio
    path('', InicioView.as_view(), name='inicio'),
    path('agregar-juegos/', agregar_juegos, name='agregar-juegos'),
    path('agregar-accesorios/', agregar_accesorios, name='agregar-accesorios'),
    path('about/', AboutView.as_view(), name='about'),
    path('consola/<int:pk>/', ConsolaDetailView.as_view(), name='detalle-consola'),
    path('crear-consola/', ConsolaCreateView.as_view(), name='crear-consola'),
    path('editar-consola/<int:pk>/', ConsolaUpdateView.as_view(), name='editar-consola'),
    path('eliminar-consola/<int:pk>/', ConsolaDeleteView.as_view(), name='eliminar-consola'),

]