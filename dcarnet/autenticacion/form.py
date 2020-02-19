from django import forms
from django.contrib.auth.models import User
from autenticacion.models import Usuarios

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UsuarioForm(forms.ModelForm):
    class Meta():
        model = Usuarios
        fields = ('tipo_usuario','foto_perfil')
