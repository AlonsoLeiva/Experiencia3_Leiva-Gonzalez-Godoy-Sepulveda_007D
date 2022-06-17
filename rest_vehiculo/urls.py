from django.urls import path
from rest_vehiculo.views import lista_personas, detalle_persona

urlpatterns =[
            path('lista_personas', lista_personas, name="lista_personas"),
            path('detalle_persona/<id>', detalle_persona, name="detalle_persona"),
            ]