from django.contrib import admin
from .models import consolas, accesorios, juegos
register_models = [consolas, accesorios, juegos]

admin.site.register(register_models)