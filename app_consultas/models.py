from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensajes(models.Model):
    remitente = models.ForeignKey(User, related_name= "msjs_enviados", on_delete= models.CASCADE)
    destinatario = models.ForeignKey(User, related_name= "msjs_recibidos", on_delete= models.CASCADE)
    mensaje = models.TextField(max_length= 1000)
    fecha_envio = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"Mensaje de {self.remitente} a {self.destinatario}"