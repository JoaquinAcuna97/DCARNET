from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
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
    template_name = "carnets/indexDoctor/medico_form.html"
    fields = [
        "nombre",
        "apellido",
        "fecha_de_nacimiento",
        "documento_de_Identidad",
        "lugar_de_nacimiento",
        "tipo_especializacion",
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
    template_name = "carnets/indexFamiliar/tutor_form.html"
    fields = [
        "nombre",
        "apellido",
        "fecha_de_nacimiento",
        "documento_de_Identidad",
        "lugar_de_nacimiento",
    ]

    def form_valid(self, form):
        form.instance.usuario = self.request.user.usuario
        return super(FamiliarCreate, self).form_valid(form)


class PerfilNinoView(DetailView):
    model = models.Nino
    context_object_name = "perfil_nino"
    template_name = "carnets/indexNino/nino_detail.html"

    def get(self, request, *args, **kwargs):
        from django.http import Http404

        try:
            nino = get_object_or_404(models.Nino, pk=kwargs["pk"])
            context = {"nino": nino}
            return render(
                request, "carnets/indexNino/nino_detail.html", context
            )
        except Http404:
            # redirect is here
            from django.shortcuts import redirect
            from django.urls import reverse_lazy

            return redirect(reverse("carnets:crear_nino"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nino"] = Nino.objects.get(self.object)
        return contex


class NinoListView(ListView):

    model = models.Nino
    paginate_by = 100  # if pagination is desired
    template_name = "carnets/indexNino/nino_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ninos_list'] = models.Nino.objects.all()
        return context


class NinoCreate(CreateView):
    model = models.Nino
    template_name = "carnets/indexNino/nino_form.html"
    fields = [
        "nombre",
        "apellido",
        "fecha_de_nacimiento",
        "documento_de_Identidad",
        "lugar_de_nacimiento",
        "servicio_de_salud",
        "medico_asignado",
    ]

    def form_valid(self, form):
        form.instance.usuario = self.request.user.usuario
        return super(NinoCreate, self).form_valid(form)


class PerfilControl_medicoView(DetailView):
    model = models.Control_medico
    context_object_name = "perfil_control_medico"
    template_name = "carnets/indexControl_medico/control_medico_detail.html"

    def get(self, request, *args, **kwargs):
        from django.http import Http404

        try:
            control_medico = get_object_or_404(models.Control_medico, pk=kwargs["pk"])
            context = {"control_medico": control_medico}
            return render(
                request, "carnets/indexControl_medico/control_medico_detail.html", context
            )
        except Http404:
            # redirect is here
            from django.shortcuts import redirect
            from django.urls import reverse_lazy

            return redirect(reverse("carnets:crear_control_medico"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["control_medico"] = Control_medico.objects.get(self.object)
        return contex


class Control_medicoCreate(CreateView):
    model = models.Control_medico
    template_name = "carnets/indexControl_medico/control_medico_form.html"
    fields = [
        "edad",
        "peso",
        "talla",
        "pd",
        "alimentacion",
        "hierro",
        "vit_D",
        "observaciones",
        "presion_arterial",
        "proximo_control",
    ]
