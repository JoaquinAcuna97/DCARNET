from django.urls import include, path
from django.conf.urls import url, include
from autenticacion import views as aviews
from . import views

app_name = "carnets"

urlpatterns = [
    url(r"^autenticacion/", include("autenticacion.urls")),
    path("controles_medicos/", views.controlesmedicos, name="ver_controles"),
    path("agregar_control/", views.agregarcontrol, name="agregar_control"),
    path("crear_persona/", views.Crear_Persona.as_view(), name="crear_persona"),
]
