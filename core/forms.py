from django import forms
from django.forms import ModelForm
from .models import PersonasDon, Vehiculo,Personas

# creamos nuestra clase para el formulario desde la base de datos
class VehiculoForm(ModelForm):


    class Meta:
        model = Vehiculo
        fields =['patente','marca','modelo','categoria']

class RegistroForm(ModelForm):

    class Meta:
        model= Personas
        fields=['nombre','apellido','rut','email','contraseña','conficontraseña','genero','estadocivil','region','direccion']

class DonanteForm(ModelForm):

    class Meta:
        model= PersonasDon
        fields=['nombre','apellido', 'pago', 'monto', 'tarjeta', 'fecha_expira', 'cvv', 'comentario']

