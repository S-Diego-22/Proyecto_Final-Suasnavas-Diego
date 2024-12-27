from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sucursales(models.Model):
    ciudad = models.CharField(max_length= 25)
    direccion = models.CharField(max_length= 50)
    imagen = models.ImageField(upload_to= "img_sucursales", null=True, blank=True)
    def __str__(self):
        return self.ciudad
    
class VentaProductos(models.Model):
    nombre = models.CharField(max_length= 20)
    descripcion = models.TextField(max_length= 500)
    imagen = models.ImageField(upload_to= "img_productos", null=True, blank=True)
    def __str__(self):
        return self.nombre

class Equipos(models.Model):
    nombre = models.CharField(max_length= 100)
    descripcion = models.TextField(max_length= 1000)
    precio = models.CharField(max_length= 15)
    imagen = models.ImageField(upload_to= "img_equipos", null=True, blank=True)
    def __str__(self):
        return self.nombre

class MedioCultivo(models.Model):
    nombre = models.CharField(max_length= 100)
    descripcion = models.TextField(max_length= 1000)
    precio = models.CharField(max_length= 15)
    imagen = models.ImageField(upload_to= "img_medio_cultivo", null=True, blank=True)
    def __str__(self):
        return self.nombre

class Reactivos(models.Model):
    nombre = models.CharField(max_length= 100)
    descripcion = models.TextField(max_length= 1000)
    precio = models.CharField(max_length= 15)
    imagen = models.ImageField(upload_to= "img_reactivos", null=True, blank=True)
    def __str__(self):
        return self.nombre

class Kits(models.Model):
    nombre = models.CharField(max_length= 100)
    descripcion = models.TextField(max_length= 1000)
    precio = models.CharField(max_length= 15)
    imagen = models.ImageField(upload_to= "img_kits", null=True, blank=True)
    def __str__(self):
        return self.nombre

class Material(models.Model):
    nombre = models.CharField(max_length= 100)
    descripcion = models.TextField(max_length= 1000)
    precio = models.CharField(max_length= 15)
    imagen = models.ImageField(upload_to= "img_material", null=True, blank=True)
    def __str__(self):
        return self.nombre
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to= "img_perfil", null=True, blank= True)

    def __str__(self):
        return self.user.username