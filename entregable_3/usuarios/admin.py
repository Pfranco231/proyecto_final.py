from django.contrib import admin
from .models import Avatar

register_models = [Avatar]

admin.site.register(register_models)