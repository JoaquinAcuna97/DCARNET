from django import forms
from django.contrib.auth.models import User
from autenticacion.models import Usuario

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class PerfilUsuarioForm(forms.ModelForm):
    class Meta():
        model = Usuario
        fields = ('tipo_usuario','foto_perfil')
