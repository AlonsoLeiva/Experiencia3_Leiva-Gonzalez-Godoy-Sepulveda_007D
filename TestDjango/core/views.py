from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Personas
from .forms import RegistroForm

# Create your views here.
def home(request):

    return render(request, 'core/inicio.html')
    

def Quienes_Somos(request):
    return render (request, 'core/Quienes somos.html')

def registro(request):
    
    return render (request, 'core/Registro.html')

def donar(request):
    return render (request, 'core/donar.html')

def Galeriafotos(request):
    return render (request, 'core/Galeriadefotos.html')


def registrar_persona(request):
    datos={

    }
    nombre=request.POST['nombres']
    apellido=request.POST['apellido']
    rut=request.POST['rut']
    email=request.POST['email']
    contraseña=request.POST['contraseña']
    conficontraseña=request.POST['contraseña2']
    genero=request.POST['genero']
    estadocivil=request.POST['estadocivil']
    region=request.POST['region']
    direccion=request.POST['dirección']

    personaencontrada=Personas.objects.filter(rut=rut)
    if personaencontrada:
        datos['mensaje']= "Error, ya existe una persona registrada con ese Rut"
        return render(request, 'core/Registro_incompleto.html',datos)
    else:
        datos['mensaje']= "Registro completado"
        persona=Personas.objects.create(nombre=nombre, apellido=apellido, rut=rut, email=email, contraseña=contraseña, conficontraseña=conficontraseña, genero=genero, estadocivil=estadocivil, region=region, direccion=direccion)
        return render(request, 'core/Registro_completo.html',datos)

def form_mod_registro(request,id):
    persona= Personas.objects.get(rut=id)

    datos= {
        'form': RegistroForm(instance=persona),
        'Persona':persona
        
    }
    return render(request, 'core/form_mod_registro.html',datos)

def editar_registro(request):
    nombre=request.POST['nombres']
    apellido=request.POST['apellido']
    rut=request.POST['rut']
    email=request.POST['email']
    contraseña=request.POST['contraseña']
    conficontraseña=request.POST['contraseña2']
    genero=request.POST['genero']
    estadocivil=request.POST['estadocivil']
    region=request.POST['region']
    direccion=request.POST['dirección']
    datos={

    }
    datos['mensaje'] = "Modificados correctamente"

    persona = Personas.objects.get(rut=rut)
    persona.nombre=nombre
    persona.apellido=apellido
    persona.email=email
    persona.contraseña=contraseña
    persona.conficontraseña=conficontraseña
    persona.genero=genero
    persona.estadocivil=estadocivil
    persona.region=region
    persona.direccion=direccion
    persona.save()

    return redirect('/')


def consultar_registro(request):
    datos={

    }
    rut=request.POST['rut']
    personas=Personas.objects.filter(rut=rut)

    if personas:
        datos['mensaje']= "Usuario encontrado correctamente"
        personax=Personas.objects.get(rut=rut)
        datos['Persona']=personax
        return render (request, 'core/Consultar-registro.html',datos)
    else:
        datos['mensaje'] = "Usuario no encontrado"
        return render (request, 'core/Consultar-registro.html',datos)

def consultar_datos(request):
    
    return render (request, 'core/Consultar-datos.html')

def registro_completo(request):
    return render (request, 'core/Registro_completo.html')
    

    


   

