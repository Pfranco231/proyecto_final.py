
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #dejamos que la app main maneje la ruta base
    path('', include('main.urls')),
]
