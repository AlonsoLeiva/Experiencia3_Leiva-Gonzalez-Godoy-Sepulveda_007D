from rest_framework import serializers
from core.models import Personas

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Personas
        fields=['nombre','apellido','rut','email','contraseña','conficontraseña','genero','estadocivil','region','direccion']