from django.urls import path
from .views import enviar_mensaje, mostrar_mensaje, consultas

urlpatterns = [
    path("consultas/", consultas, name= "consultas"),
    path("enviar_mensaje/", enviar_mensaje, name= "enviar mensaje"),
    path("mostrar_mensaje/", mostrar_mensaje, name= "mostrar mensajes")
]
