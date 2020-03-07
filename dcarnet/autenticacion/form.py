from django import forms
from django.contrib.auth.models import User
from autenticacion.models import Usuario
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class UsuarioForm(forms.ModelForm):
    username = UsernameField(
        label=("Usuario"),
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "autofocus": True,
                "placeholder": "Ingrese nombre de usuario",
            }
        ),
    )
    password = forms.CharField(
        label=("Contraseña"),
        widget=forms.PasswordInput(
            attrs={"class": "input", "placeholder": "Ingrese Contraseña"}
        ),
    )
    email = forms.CharField(
        label=("Correo Electronico"),
        widget=forms.EmailInput(
            attrs={"class": "input", "placeholder": "Direccion de correo Electronico"}
        ),
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

    error_messages = {
        "invalid_login": (
            "Usuario y/o Contraseña invalidas. "
            "Recuerde que los dos campos son sensibles a mayusculas."
        ),
        "inactive": ("Cuenta Desactivada."),
    }


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ("tipo_usuario", "foto_perfil")


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label=("Usuario"),
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "autofocus": True,
                "placeholder": "Ingrese nombre de usuario",
            }
        ),
    )
    password = forms.CharField(
        label=("Contraseña"),
        widget=forms.PasswordInput(
            attrs={"class": "input", "placeholder": "Ingrese Contraseña"}
        ),
    )
    error_messages = {
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
