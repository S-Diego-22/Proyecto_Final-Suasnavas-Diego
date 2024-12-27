from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Mensajes


# Create your views here.
def consultas(request):
    return render(request, "app_consultas/consultas.html")

def enviar_mensaje(request):
    if request.method == "POST":
        username_destinatario = request.POST.get("destinatario")
        mensaje = request.POST.get("mensaje")
        destinatario = User.objects.get(username = username_destinatario)
        Mensajes.objects.create(remitente = request.user, destinatario = destinatario, mensaje = mensaje)
        return redirect("mostrar mensajes")
    
    usuarios = User.objects.exclude(username = request.user.username)

    return render(request, "app_consultas/enviar_mensaje.html", {"usuarios": usuarios})

def mostrar_mensaje(request):
    enviados = Mensajes.objects.filter(remitente=request.user)
    recibidos = Mensajes.objects.filter(destinatario=request.user)
    chat = (enviados | recibidos).order_by("-fecha_envio")
    return render(request, "app_consultas/mostrar_mensaje.html", {"chat": chat})