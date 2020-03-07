from django import forms
from django.contrib.auth.models import User
from autenticacion.models import Usuario
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class UsuarioForm(forms.ModelForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={"class": "input", "autofocus": True, "placeholder": "Usuario"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "input", "placeholder": "Contraseña"}
        )
    )

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


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "autofocus": True,
                "placeholder": "Usuario",
                "label": "Usuario",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "input",
                "placeholder": "Contraseña",
                "label": "Contraseña",
            }
        )
    )
    error_messages = {
        "username": {"max_length": ("Ese nombre de usuario es muy largo"),},
        "invalid_login": (
            "Usuario y/o Contraseña invalidas. "
            "Recuerde que los dos campos son sensibles a mayusculas."
        ),
        "inactive": ("Cuenta Desactivada."),
    }

    class Meta:
        model = User
        fields = ("username", "password")
        help_texts = {
            "username": ("Ingrese nombre de usuario."),
        }
