from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import PersonasDon, Vehiculo,Curso,Personas 
from .forms import RegistroForm, VehiculoForm, DonanteForm

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

    datos['mensaje']= "Donacion completada"
    donante=PersonasDon.objects.create(nombre=nombre, apellido=apellido, pago=pago, monto=monto, tarjeta=tarjeta, fecha_expira=fecha_expira, cvv=cvv, comentario=comentario)
    return render(request, 'core/donar.html',datos)

def form_mod_donacion(request,id):
    donante = PersonasDon.objects.get(tarjeta=id)
    datos= {
        'form': DonanteForm(instance=donante),
        'Donante':donante
    }
    return render(request, 'core/form_mod_donacion.html',datos)

def editar_donacion(request):
    nombre=request.POST['nombre']
    apellido=request.POST['apellido']
    pago=request.POST['metodo']
    monto =request.POST['monto']
    tarjeta =request.POST['Numerotarjeta']
    fecha_expira =request.POST['fecha']
    cvv =request.POST['cvv']
    comentario=request.POST['comentario']
    datos={

    }
    datos['mensaje'] = "Modificados correctamente"

    donante = PersonasDon.objects.get(tarjeta=tarjeta)
    donante.nombre=nombre
    donante.apellido=apellido
    donante.pago=pago
    donante.monto=monto
    donante.tarjeta=tarjeta
    donante.fecha_expira=fecha_expira
    donante.cvv=cvv
    donante.comentario=comentario
    donante.save()

    return render(request, 'core/Registro_completo.html',datos)

    


   

