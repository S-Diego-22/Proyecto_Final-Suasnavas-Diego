from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm, EditUserForm, FotoPerfilForm
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, "app_paginas/inicio.html")

def quines_somos(request):
    return render(request, "app_paginas/quienes_somos.html")

def sucursales(request):
    sucursal = Sucursales.objects.all()
    return render(request, "app_paginas/sucursales.html", {"sucursal": sucursal})

def venta_productos(request):
    productos = VentaProductos.objects.all()
    return render(request, "app_paginas/venta_productos.html", {"productos": productos})
# Esto va dentro de la pagina venta_productos
def equipos(request):
    articulos = Equipos.objects.all()
    return render(request, "app_paginas/productos/equipos.html", {"articulos": articulos})

def medio_cultivo(request):
    articulos = MedioCultivo.objects.all()
    return render(request, "app_paginas/productos/medio_cultivo.html", {"articulos": articulos})

def reactivos(request):
    articulos = Reactivos.objects.all()
    return render(request, "app_paginas/productos/reactivos.html", {"articulos": articulos})

def kits(request):
    articulos = Kits.objects.all()
    return render(request, "app_paginas/productos/kits.html", {"articulos": articulos})

def material(request):
    articulos = Material.objects.all()
    return render(request, "app_paginas/productos/material.html", {"articulos": articulos})

@login_required(login_url= "login")
def compras(request):
    return render(request, "app_paginas/compras.html")
# Aca finaliza.

#formularios

def login_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("inicio") 
        else:
            return redirect("inicio")
    return render(request, "app_paginas/formularios/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("inicio")
    else:
        form = RegisterUserForm()
    return render(request, "app_paginas/formularios/register.html", {"form": form})

def ver_perfil(request):
    usuario = request.user
    return render(request, "app_paginas/formularios/ver_perfil.html", {"usuario": usuario})

def editar_perfil(request):
    usuario = request.user
    perfil, _ = Perfil.objects.get_or_create(user = usuario)
    if request.method == "POST":
        formulario = EditUserForm(request.POST, instance= usuario)
        photo = FotoPerfilForm(request.POST, request.FILES, instance= perfil)
        if formulario.is_valid() and photo.is_valid():
            formulario.save()
            photo.save()
            return redirect("ver perfil")
        else:
            return redirect("inicio")
    else:
        formulario = EditUserForm(instance= usuario)
        photo = FotoPerfilForm(instance= usuario)

    return render(request, "app_paginas/formularios/editar_perfil.html", {"formulario": formulario, "photo": photo})

def cambiar_clave(request):
    usuario = request.user
    if request.method == "POST":
        clave = PasswordChangeForm(usuario, request.POST)
        if clave.is_valid():
            clave.save()
            return redirect("login")
    else:
        clave = PasswordChangeForm(usuario)
    return render(request, "app_paginas/formularios/cambiar_clave.html", {"clave": clave})