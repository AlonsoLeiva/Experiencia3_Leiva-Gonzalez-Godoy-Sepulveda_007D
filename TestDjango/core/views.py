from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Donaciones, Personas 
from .forms import RegistroForm,  DonanteForm

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

#Registrar Personas
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
        return render(request, 'core/Registro_resultado.html',datos)
    else:
        datos['mensaje']= "Registro completado"
        persona=Personas.objects.create(nombre=nombre, apellido=apellido, rut=rut, email=email, contraseña=contraseña, conficontraseña=conficontraseña, genero=genero, estadocivil=estadocivil, region=region, direccion=direccion)
        return render(request, 'core/Registro_resultado.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Modificar Personas
def form_mod_registro(request,id):
    persona= Personas.objects.get(rut=id)

    datos= {
        'form': RegistroForm(instance=persona),
        'Persona':persona
        
    }
    return render(request, 'core/form_mod_registro.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Mandar para modificar
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

    return render(request, 'core/Registro_resultado.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Consulta de registro
def consultar_registro(request):
    datos={

    }
    rut=request.POST['rut']
    contraseña=request.POST['contraseña']
    personas=Personas.objects.filter(rut=rut)
    personabuscada=Personas.objects.filter(contraseña=contraseña)

    if personas and personabuscada:
        datos['mensaje']= "Usuario encontrado correctamente"
        personax=Personas.objects.get(rut=rut)
        datos['Persona']=personax
        return render (request, 'core/Consultar-registro.html',datos)
    elif personas:
        datos['mensaje']= "Usuario encontrado pero contraseña incorrecta"
        return render (request, 'core/Consultar-registro.html',datos)
    else:
        datos['mensaje'] = "Usuario no encontrado"
        return render (request, 'core/Consultar-registro.html',datos)
#---------------------------------------------------------------------------------------------------------------------
def consultar_datos(request):
    
    return render (request, 'core/Consultar-datos.html')

def registro_completo(request):
    return render (request, 'core/Registro_resultado.html')
#---------------------------------------------------------------------------------------------------------------------
#Registro de donante
def registrar_donante(request):
    datos={

    }
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    pago=request.POST['metodo']
    monto =request.POST['monto']
    tarjeta =request.POST['Numerotarjeta']
    fecha_expira =request.POST['fecha']
    cvv =request.POST['cvv']
    comentario=request.POST['comentario']
    todaspersonas=Donaciones.objects.all()
    cantpersonas=1
    for i in todaspersonas:
        cantpersonas=cantpersonas+1




    
    datos['cantidad']=cantpersonas

    datos['mensaje']= "Donacion completada"
    donante=Donaciones.objects.create(id=cantpersonas ,nombre=nombre, apellido=apellido, pago=pago, monto=monto, tarjeta=tarjeta, fecha_expira=fecha_expira, cvv=cvv, comentario=comentario)
    return render(request, 'core/Registro_resultado.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Pagina de modificacion
def form_mod_donacion(request,id):
    donante = Donaciones.objects.get(id=id)
    datos= {
        'form': DonanteForm(instance=donante),
        'Donante':donante
    }
    return render(request, 'core/form_mod_donar.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Mandar para modificar donaciones
def editar_donacion(request):
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    pago=request.POST['metodo']
    monto =request.POST['monto']
    tarjeta =request.POST['Numerotarjeta']
    fecha_expira =request.POST['fecha']
    cvv =request.POST['cvv']
    comentario=request.POST['comentario']
    id=request.POST['id']
    datos={

    }
    datos['mensaje'] = "Modificados correctamente"

    donante = Donaciones.objects.get(id=id)
    donante.nombre=nombre
    donante.apellido=apellido
    donante.pago=pago
    donante.monto=monto
    donante.tarjeta=tarjeta
    donante.fecha_expira=fecha_expira
    donante.cvv=cvv
    donante.comentario=comentario
    donante.save()

    return render(request, 'core/Registro_resultado.html',datos)
#---------------------------------------------------------------------------------------------------------------------
#Pagina para consultar donaciones
def consultar_donacion(request):
    datos={

    }
    tarjeta=request.POST['tarjeta']
    donaciones=Donaciones.objects.filter(tarjeta=tarjeta)

    if donaciones:
        datos['mensaje']= "Donacion encontrada correctamente"
        donacionx=Donaciones.objects.filter(tarjeta=tarjeta)
        datos['Donacion']=donacionx
        return render (request, 'core/Consultar-registro-donar.html',datos)
    else:
        datos['mensaje'] = "Donación no encontrada"
        return render (request, 'core/Consultar-registro-donar.html',datos)
#---------------------------------------------------------------------------------------------------------------------
def consultar_donar(request):
    
    return render (request, 'core/Consultar-datos-donar.html')

    


   

