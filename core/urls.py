from django.urls import path
from .views import home,donar,Galeriafotos,Quienes_Somos,registro


urlpatterns = [
    path ('', home,name="home"), 
    path ('QuienesSomos', Quienes_Somos,name="Quienes_Somos"),
    path ('form-registro', registro,name="registro"),
    path ('form-donar', donar,name="donar"),
    path ('Galeria', Galeriafotos,name="Galeriafotos"),


]