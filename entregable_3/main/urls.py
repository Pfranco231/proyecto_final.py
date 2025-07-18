from django.urls import path
from .views import inicio

urlpatterns = [
    # Ruta para la vista de inicio
    path('', inicio, name='inicio'),
]