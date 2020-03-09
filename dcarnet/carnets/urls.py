from django.urls import include, path
from django.conf.urls import url, include
from autenticacion import views as aviews
from . import views

app_name = "carnets"

urlpatterns = [
    url(r"^autenticacion/", include("autenticacion.urls")),
    path("controles_medicos/", views.controlesmedicos, name="Ver_controles"),
    path("agregar_control/", views.agregarcontrol, name="Agregar_control"),
    path(
        "detail_Medico/<int:pk>/",
        views.PerfilMedicoView.as_view(),
        name="detail_medico",
    ),
    path("Crear_Medico/", views.MedicoCreate.as_view(), name="crear_medico"),
    path(
        "detail_Familiar/<int:pk>/",
        views.PerfilFamiliarView.as_view(),
        name="detail_Familiar",
    ),
    path("Crear_Familiar/", views.FamiliarCreate.as_view(), name="crear_familiar"),
]
