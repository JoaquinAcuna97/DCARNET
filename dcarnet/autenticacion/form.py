from django import forms
from django.contrib.auth.models import User
from autenticacion.models import Usuario


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")

        labels = {
            "username": ("Usuario"),
        }
        help_texts = {
            "username": ("Ingrese nombre de usuario."),
        }
        error_messages = {
            "username": {"max_length": ("Ese nombre de usuario es muy largo"),},
        }


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ("tipo_usuario", "foto_perfil")
