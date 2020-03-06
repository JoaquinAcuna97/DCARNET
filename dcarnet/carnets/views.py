from django.shortcuts import render
from django.forms.models import model_to_dict
from django.views.generic import DetailView
from autenticacion import models as authmodels
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


def create_person(user):
    if user.usuario.tipo_usuario == "b":
        print("# se creo un doctor para este usuario!")
        pers = models.Persona.objects.create(usuario_ptr=user.usuario, tipo_persona="b")
        doc = models.Medico.objects.create(persona_ptr=pers)
    else:
        print("# se creo un familiar para este usuario!")
        pers = models.Persona.objects.create(usuario_ptr=user.usuario, tipo_persona="a")
        fami = models.Tutor.objects.create(persona_ptr=pers)
