from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import DetailView

from django.http import HttpResponse
from . import models

# update and create views


def controlesmedicos(request):
    # control= Control.objects.all()
    # return render(request, 'carnets/icontrolmedico.html', {'control': control})
    return render(request, "carnets/agregarcontrol.html")


def agregarcontrol(request):

    return render(request, "carnets/agregarcontrol.html")


class DetailViewNino(DetailView):
    model = models.Nino

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["lista_ninos"] = models.Nino.objects.all()
        return context


class PersonaCreate(CreateView):
    model = models.Persona
    fields = [
        "nombre",
        "apellido",
        "fecha_de_nacimiento",
        "documento_de_Identidad",
        "lugar_de_nacimiento",
    ]


class MedicoCreate(CreateView):
    model = models.Medico
    fields = [
        "nombre",
        "apellido",
        "fecha_de_nacimiento",
        "documento_de_Identidad",
        "lugar_de_nacimiento",
        "tipo_especializacion",
        "fecha_de_creacion",
    ]


class FamiliarCreate(CreateView):
    model = models.Tutor
    fields = [
        "nombre",
        "apellido",
        "fecha_de_nacimiento",
        "documento_de_Identidad",
        "lugar_de_nacimiento",
        "hijos",
        "agenda",
    ]
