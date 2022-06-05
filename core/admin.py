from django.contrib import admin
from .models import Personas,Donaciones

# Register your models here.
# Permite administrar el modelo completo


admin.site.register(Personas)
admin.site.register(Donaciones)