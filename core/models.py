from django.db import models

# Create your models here.


#modelo categoria

class Categoria(models.Model):
    idCategoria=models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria=models.CharField(max_length=50, verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria


class Civil(models.Model):
    idCivil=models.IntegerField(primary_key=True, verbose_name='Id de estado civil')
    nombreCivil=models.CharField(max_length=50,verbose_name='Nombre estado civil')

    def __str__(self):
        return self.nombreCivil

class Genero(models.Model):
    idgenero=models.IntegerField(primary_key=True,verbose_name='Id género')
    NombreGenero=models.CharField(max_length=50,verbose_name='Nombre Género')

    def __str__(self):
        return self.NombreGenero

class Region(models.Model):
    idregion=models.IntegerField(primary_key=True,verbose_name='Id Region')
    NombreRegion=models.CharField(max_length=50,verbose_name='Nombre Region')

    def __str__(self):
        return self.NombreRegion


#modelo para el vehiculo

class Vehiculo(models.Model):
    patente=models.CharField(max_length=6,primary_key=True,verbose_name='Patente')
    marca=models.CharField(max_length=20,verbose_name='Marca vehiculo')
    modelo=models.CharField(max_length=20,null=True,blank=True,verbose_name='Modelo')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) :
        return self.patente

class Curso(models.Model):
    nombre=models.CharField(max_length=30)
    creditos=models.PositiveBigIntegerField()
    docente=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre, self.creditos

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
        return self.nombre, self.apellido, self.rut, self.email, self.contraseña, self.conficontraseña, self.genero, self.estadocivil, self.region, self.direccion

    
class PersonasDon(models.Model):
    nombre=models.CharField(max_length=100,verbose_name='Nombres')
    apellido=models.CharField(max_length=100,verbose_name='Apellidos')
    pago=models.CharField(max_length=100,verbose_name='Pago')
    monto=models.CharField(max_length=200,verbose_name='Monto')
    tarjeta=models.CharField(max_length=100, primary_key=True, verbose_name='Tarjeta')
    fecha_expira=models.CharField(max_length=100,verbose_name='Fecha de expiracion')
    cvv=models.CharField(max_length=100,verbose_name='CVV')
    comentario=models.CharField(max_length=100,verbose_name='Comentario')

    def __str__(self):
        return self.nombre, self.apellido, self.pago, self.monto, self.tarjeta, self.fecha_expira, self.cvv, self.comentario