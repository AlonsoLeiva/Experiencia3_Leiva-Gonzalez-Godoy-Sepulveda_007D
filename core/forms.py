from django import forms
from django.forms import ModelForm
from .models import Vehiculo,Registro

# creamos nuestra clase para el formulario desde la base de datos
class VehiculoFrom(ModelForm):


    class Meta:
        model=Vehiculo
        fields=['patente','marca','modelo','categoria']

class registration(ModelForm):

    class Meta:
        model=Registro
        fields=['Nombres','Apellidos','Rut','Email','Contraseña','Confirmar Contraseña','Género','Estado Civil','Region','Dirección']

