from django.urls import path
from .views import home,Test,form_vehiculo,form_mod_vehiculo,form_del_vehiculo,donar,Galeriafotos,registro,Quienes_Somos,registrar_curso,registrar_persona


urlpatterns = [
    path ('', home,name="home"), 
    path ('test', Test,name="Test"),
    path ('form-vehiculo', form_vehiculo,name="form_vehiculo"),
    path ('form-mod-vehiculo/<id>', form_mod_vehiculo,name="form_mod_vehiculo"),
    path ('form-del-vehiculo/<id>', form_del_vehiculo,name="form_del_vehiculo"),
    path ('QuienesSomos', Quienes_Somos,name="Quienes_Somos"),
    path ('form-registro', registro,name="registro"),
    path ('form-donar', donar,name="donar"),
    path ('Galeria', Galeriafotos,name="Galeriafotos"),
    path ('registrarCurso/', registrar_curso),
    path ('registrarPersona/', registrar_persona),
]