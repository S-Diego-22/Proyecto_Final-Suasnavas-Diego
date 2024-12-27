from django.urls import path
from app_paginas.views import *

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("quienes_somos/", quines_somos, name= "quienes somos"),
    path("sucursales/", sucursales, name= "sucursales"),
    path("venta_productos", venta_productos, name= "venta de productos"),
    # equipos, medio_cultivo, reactivos, kits y material. Van dentro de la pagina de venta_productos
    path("equipos/", equipos, name= "equipos"),
    path("medio_cultivos/", medio_cultivo, name= "medios de cultivo"),
    path("reactivos/", reactivos, name= "reactivos"),
    path("kits/", kits, name= "kits"),
    path("material/", material, name= "material"),
    path("compras/", compras, name= "compras"),
    # formularios
    path("login/", login_usuario, name= "login"),
    path("logout/", user_logout, name= "logout"),
    path("register/", register, name= "register"),
    path("ver_perfil/", ver_perfil, name= "ver perfil"),
    path("editar_perfil/", editar_perfil, name= "editar perfil"),
    path("cambiar_clave/", cambiar_clave, name= "cambiar clave"),
]