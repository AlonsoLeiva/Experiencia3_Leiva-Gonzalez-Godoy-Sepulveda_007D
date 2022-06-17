from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Personas
from .serializers import PersonasSerializer
from rest_vehiculo import serializers
@csrf_exempt
@api_view(['GET','POST'])
# Create your views here.
def lista_personas(request):
    """
    Lista de todas las Personas
    """
    if request.method =='GET':
        personas = Personas.objects.all()
        serializer = PersonasSerializer(personas, many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        #data= JSONParser().parse(request)
        serializer = PersonasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_persona(request, id):
    """
    Get, update o delete de una persona en particular
    """
    try:
        persona= Personas.objects.get(rut=id)
    except Personas.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PersonasSerializer(persona)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer= PersonasSerializer(persona, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method =='DELETE':
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
