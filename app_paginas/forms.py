from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length= 15, required= True, label= "Nombre de usuario")
    first_name = forms.CharField(max_length= 20, required=True, label= "Nombre")
    last_name = forms.CharField(max_length= 20, required=True, label= "Apellido")
    email = forms.EmailField(max_length= 50, required=True, label= "Correo electrónico")
    password1 = forms.CharField(max_length= 20, 
                                min_length= 8, 
                                required=True, 
                                label= "Contraseña", 
                                help_text= "Su contraseña debe tener entre 8 a 20 caracteres y debe ser alfanumérica",
                                widget=forms.PasswordInput(attrs={'style': 'width: 200px;'}))
    password2 = forms.CharField(max_length= 20, 
                                min_length= 8, 
                                required=True, 
                                label= "Confirmar contraseña",
                                widget=forms.PasswordInput(attrs={'style': 'width: 200px;'}))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name","email", "password1", "password2"]

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email"]

class FotoPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["photo"]