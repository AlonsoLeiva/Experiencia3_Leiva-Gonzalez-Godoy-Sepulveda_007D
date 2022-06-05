from django import forms
from django.forms import ModelForm
from .models import Personas

# creamos nuestra clase para el formulario desde la base de datos


class RegistroForm(ModelForm):

    class Meta:
        model= Personas
        fields=['nombre','apellido','rut','email','contraseña','conficontraseña','genero','estadocivil','region','direccion']

