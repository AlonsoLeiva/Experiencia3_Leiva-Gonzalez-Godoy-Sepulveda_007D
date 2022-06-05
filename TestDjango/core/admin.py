from django.contrib import admin
from .models import Categoria, Vehiculo,Genero,Civil,Region,Curso,Personas

# Register your models here.
# Permite administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Vehiculo)
admin.site.register(Genero)
admin.site.register(Civil)
admin.site.register(Region)
admin.site.register(Curso)
admin.site.register(Personas)