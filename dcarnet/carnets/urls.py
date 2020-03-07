from django.urls import include, path
from django.conf.urls import url, include
from autenticacion import views as aviews
from . import views

app_name = "carnets"

urlpatterns = [
    url(r"^autenticacion/", include("autenticacion.urls")),
    path("controles_medicos/", views.controlesmedicos, name="Ver_controles"),
    path("agregar_control/", views.agregarcontrol, name="Agregar_control"),
    path("Crear_Persona/", views.PersonaCreate.as_view(), name="crear_persona"),
    path("Crear_Medico/", views.MedicoCreate.as_view(), name="crear_medico"),
    path("Crear_Familiar/", views.FamiliarCreate.as_view(), name="crear_familiar"),
]
