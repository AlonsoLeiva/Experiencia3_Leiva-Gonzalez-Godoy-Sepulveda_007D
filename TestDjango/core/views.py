from django.shortcuts import render, redirect
from .models import Vehiculo,Curso,Personas
from .forms import RegistroForm, VehiculoForm

# Create your views here.
def home(request):

    return render(request, 'core/inicio.html')
    

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


def Test(request):
    vehiculos=Vehiculo.objects.all()
    lista=["Lasaña", "Charquicán", "Porotos granados"]
    hijo=Persona("Fernando Rivera","4")
    contexto={"nombre":"Claudia Andrea", "comidas":lista, "hijo":hijo, 'Vehiculos':vehiculos}
    


    return render(request, 'core/test.html', contexto )

def form_mod_vehiculo(request,id):
    vehiculo= Vehiculo.objects.get(patente=id)

    datos= {
        'form': VehiculoForm(instance=vehiculo)
        
    }
    if request.method=='POST':
        formulario= VehiculoForm(data=request.POST,instance=vehiculo)
        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/form_mod_vehiculo.html',datos)

def form_vehiculo(request):
    vehiculos=Vehiculo.objects.all()
    datos = {
        'form': VehiculoForm(),
        'Vehiculos':vehiculos
    }
    if request.method== 'POST':
        formulario = VehiculoForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render (request, 'core/form_vehiculo.html',datos)

def form_del_vehiculo(request, id):
    vehiculos=Vehiculo.objects.get(patente=id)
    vehiculos.delete()

    return redirect(to="home")

def Quienes_Somos(request):
    return render (request, 'core/Quienes somos.html')

def registro(request):
    datos = {
        'form': RegistroForm()
    }
    if request.method== 'POST':
        formulario = RegistroForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render (request, 'core/Registro.html',datos)

def donar(request):
    return render (request, 'core/donar.html')

def Galeriafotos(request):
    return render (request, 'core/Galeriadefotos.html')

def registrar_curso(request):
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso=Curso.objects.create(nombre=nombre, creditos=creditos)
    return redirect('/')

def registrar_persona(request):
    nombre=request.POST['nombres']
    apellido=request.POST['apellido']
    rut=request.POST['rut']
    email=request.POST['email']
    contraseña=request.POST['contraseña']
    conficontraseña=request.POST['contraseña2']
    region=request.POST['region']
    direccion=request.POST['dirección']

    persona=Personas.objects.create(nombre=nombre, apellido=apellido, rut=rut, email=email, contraseña=contraseña, conficontraseña=conficontraseña, region=region, direccion=direccion)
    return redirect('/')


