from django.urls import path
from .views import consultar_datos, home,Test,form_vehiculo,form_mod_vehiculo,form_del_vehiculo,donar,Galeriafotos,registro,Quienes_Somos,registrar_persona,form_mod_registro,editar_registro,consultar_registro,consultar_datos,registro_completo, registrar_donante, form_mod_donacion, editar_donacion


urlpatterns = [
    path ('', home,name="home"), 
    path ('test', Test,name="Test"),
    path ('form-vehiculo', form_vehiculo,name="form_vehiculo"),
    path ('form-mod-vehiculo/<id>', form_mod_vehiculo,name="form_mod_vehiculo"),
    path ('form-del-vehiculo/<id>', form_del_vehiculo,name="form_del_vehiculo"),
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
    path ('form-mod-donacion/<id>', form_mod_donacion, name="form_mod_donacion"),
    path ('editar-donacion/', editar_donacion, name="editar_donacion"),
]

