from django.urls import path
from .views import consultar_datos, home,donar,Galeriafotos,registro,Quienes_Somos,registrar_persona,form_mod_registro,editar_registro,consultar_registro,consultar_datos, registrar_donante, form_mod_donacion, editar_donacion,consultar_donar,consultar_donacion


urlpatterns = [
    path ('', home,name="home"), 
    path ('QuienesSomos', Quienes_Somos,name="QuienesSomos"),
    path ('form-registro', registro,name="form-registro"),
    path ('Galeria', Galeriafotos,name="Galeria"),
    path ('registrarPersona/', registrar_persona),
    path ('form-mod-registro/<id>', form_mod_registro, name="form_mod_registro"),
    path ('Editar-registro/', editar_registro, name="Editar_registro"),
    path ('Consultar-datos', consultar_datos, name="Consultar_datos"),
    path ('Consultar-registro/', consultar_registro, name="Consultar_registro"),
    path ('form-donar', donar, name="form-donar"),
    path ('registrar_donante/', registrar_donante),
    path ('form-mod-donar/<id>', form_mod_donacion, name="form_mod_donacion"),
    path ('editar-donacion/', editar_donacion, name="editar_donacion"),
    path ('Consultar-donar', consultar_donar, name="Consultar_datos_donar"),
    path ('Consultar-donacion/', consultar_donacion, name="Consultar_donacion"),
]

