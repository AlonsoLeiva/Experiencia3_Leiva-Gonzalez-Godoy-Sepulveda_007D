from django.urls import path
from .views import consultar_datos, home,donar,Galeriafotos,registro,Quienes_Somos,registrar_persona,form_mod_registro,editar_registro,consultar_registro,consultar_datos,registro_completo


urlpatterns = [
    path ('', home,name="home"), 
    path ('QuienesSomos', Quienes_Somos,name="QuienesSomos"),
    path ('form-registro', registro,name="form-registro"),
    path ('form-donar', donar,name="form-donar"),
    path ('Galeria', Galeriafotos,name="Galeria"),
    path ('registrarPersona/', registrar_persona),
    path ('form-mod-registro/<id>', form_mod_registro,name="form_mod_registro"),
    path ('Editar-registro/', editar_registro,name="Editar_registro"),
    path ('Consultar-datos', consultar_datos,name="Consultar_datos"),
    path ('Consultar-registro/', consultar_registro,name="Consultar_registro"),
]