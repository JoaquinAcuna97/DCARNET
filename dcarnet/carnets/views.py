from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from . import models
from django.urls import reverse

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


class PerfilMedicoView(DetailView):
    model = models.Medico
    context_object_name = "perfil_medico"
    template_name = "carnets/indexDoctor/doctor_detail.html"

    def get(self, request, *args, **kwargs):
        from django.http import Http404

        try:
            medico = get_object_or_404(models.Medico, pk=kwargs["pk"])
            context = {"medico": medico}
            return render(request, "carnets/indexDoctor/doctor_detail.html", context)
        except Http404:
            # redirect is here
            from django.shortcuts import redirect
            from django.urls import reverse_lazy

            return redirect(reverse("carnets:crear_medico"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["medico"] = Tutor.objects.get(self.object)
        return contex


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

    def form_valid(self, form):
        form.instance.usuario = self.request.user.usuario
        return super(MedicoCreate, self).form_valid(form)


class PerfilFamiliarView(DetailView):
    model = models.Tutor
    context_object_name = "perfil_familiar"
    template_name = "carnets/indexFamiliar/familiar_detail.html"

    def get(self, request, *args, **kwargs):
        from django.http import Http404

        try:
            tutor = get_object_or_404(models.Tutor, pk=kwargs["pk"])
            context = {"tutor": tutor}
            return render(
                request, "carnets/indexFamiliar/familiar_detail.html", context
            )
        except Http404:
            # redirect is here
            from django.shortcuts import redirect
            from django.urls import reverse_lazy

            return redirect(reverse("carnets:crear_familiar"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tutor"] = Tutor.objects.get(self.object)
        return contex


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

    def form_valid(self, form):
        form.instance.usuario = self.request.user.usuario
        return super(FamiliarCreate, self).form_valid(form)
