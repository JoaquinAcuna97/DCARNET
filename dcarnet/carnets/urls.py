from django.urls import include, path
from django.conf.urls import url, include
from autenticacion import views as aviews
from . import views

app_name = "carnets"

urlpatterns = [
    url(r"^autenticacion/", include("autenticacion.urls")),
    path(
        "detail_Medico/<int:pk>/",
        views.PerfilMedicoView.as_view(),
        name="detail_medico",
    ),
    path("Crear_Medico/", views.MedicoCreate.as_view(), name="crear_medico"),
    path(
        "detail_Familiar/<int:pk>/",
        views.PerfilFamiliarView.as_view(),
        name="detail_familiar",
    ),
    path("Crear_Familiar/", views.FamiliarCreate.as_view(), name="crear_familiar"),
    path("detail_Nino/<int:pk>/", views.PerfilNinoView.as_view(), name="detail_nino",),
    path("list_nino/", views.NinoListView.as_view(), name="nino_list"),
    path("Crear_Nino/", views.NinoCreate.as_view(), name="crear_nino"),
    path(
        "detail_Control_medico/<int:pk>/",
        views.Perfil_Control_medico_View.as_view(),
        name="detail_Control_medico",
    ),
    path(
        "Crear_Control_medico/",
        views.Control_medicoCreate.as_view(),
        name="crear_control_medico",
    ),
    path(
        "list_control_medico",
        views.Control_medico_List_View.as_view(),
        name="control_list",
    ),
]
