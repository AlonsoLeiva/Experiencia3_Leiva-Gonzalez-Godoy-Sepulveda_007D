from django.shortcuts import render

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

