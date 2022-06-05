from django.db import models

# Create your models here.


#modelo categoria


class Personas(models.Model):
    nombre=models.CharField(max_length=100,verbose_name='Nombres')
    apellido=models.CharField(max_length=100,verbose_name='Apellidos')
    rut=models.CharField(max_length=100,primary_key=True,verbose_name='Rut')
    email=models.CharField(max_length=200,verbose_name='Email')
    contraseña=models.CharField(max_length=100,verbose_name='Contraseña')
    conficontraseña=models.CharField(max_length=100,verbose_name='Confirmar Contraseña')
    genero=models.CharField(max_length=100,verbose_name='Género')
    estadocivil=models.CharField(max_length=100,verbose_name='Estado Civil')
    region=models.CharField(max_length=100,verbose_name='Region')
    direccion=models.CharField(max_length=100,verbose_name='Dirección')

    def __str__(self):
        return self.rut

    
class Donaciones(models.Model):
    id=models.CharField(max_length=100,primary_key=True,verbose_name='Id de Donación')
    nombre=models.CharField(max_length=100,verbose_name='Nombres')
    apellido=models.CharField(max_length=100,verbose_name='Apellidos')
    pago=models.CharField(max_length=100,verbose_name='Pago')
    monto=models.CharField(max_length=200,verbose_name='Monto')
    tarjeta=models.CharField(max_length=100, verbose_name='Tarjeta')
    fecha_expira=models.CharField(max_length=100,verbose_name='Fecha de expiracion')
    cvv=models.CharField(max_length=100,verbose_name='CVV')
    comentario=models.CharField(max_length=100,blank=True,verbose_name='Comentario')

    def __str__(self):
        return self.id
