from django import forms
from django.forms import ModelForm
from .models import Vehiculo,Personas

# creamos nuestra clase para el formulario desde la base de datos
class VehiculoForm(ModelForm):


    class Meta:
        model = Vehiculo
        fields =['patente','marca','modelo','categoria']

class RegistroForm(ModelForm):

    class Meta:
        model= Personas
        fields=['nombre','apellido','rut','email','contraseña','conficontraseña','genero','estadocivil','region','direccion']

