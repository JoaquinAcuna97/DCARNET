from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from . import models
from autenticacion import models as authmodels
from django.urls import reverse
from django import forms

# update and create views


class PerfilMedicoView(DetailView):
    model = models.Medico
    context_object_name = "perfil_medico"
    template_name = "carnets/indexDoctor/doctor_detail.html"

    def get(self, request, *args, **kwargs):
        from django.http import Http404

        try:
            medico = get_object_or_404(models.Medico, usuario_id=kwargs["pk"])
            context = {"medico": medico}
            return render(request, "carnets/indexDoctor/doctor_detail.html", context)
        except Http404:
            # redirect is here
            from django.shortcuts import redirect
            from django.urls import reverse_lazy

            print("NO ENCONTRAMOS al medico.....")
            return redirect(reverse("carnets:crear_medico"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["medico"] = models.Tutor.objects.get(self.object)
        return context


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
            tutor = get_object_or_404(models.Tutor, usuario_id=kwargs["pk"])
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
        context["tutor"] = models.Tutor.objects.get(self.object)
        return context


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
            return render(request, "carnets/indexNino/nino_detail.html", context)
        except Http404:
            # redirect is here
            from django.shortcuts import redirect
            from django.urls import reverse_lazy

            return redirect(reverse("carnets:crear_nino"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nino"] = models.Nino.objects.get(self.object)
        return context


class NinoListView(ListView):

    model = models.Nino
    paginate_by = 100  # if pagination is desired
    template_name = "carnets/indexNino/nino_list.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["ninos_list"] = models.Nino.objects.all()
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # try/cach si no esta el usuario enviar a create medico
        usuario = authmodels.Usuario.objects.get(id=self.kwargs["pk"])
        print("el usuario es:" + "pk: " + str(usuario.id))

        if usuario.tipo_usuario == "b":
            print("el usuario es DOCTOR:" + "pk: " + str(usuario.id))
            medico = models.Medico.objects.get(usuario_id=usuario.id)
            context["ninos_list"] = medico.nino_set.all()
        elif usuario.tipo_usuario == "a":
            print("el usuario es TUTOR:" + "pk: " + str(usuario.id))
            familiar = models.Tutor.objects.get(usuario_id=usuario.id)
            context["ninos_list"] = familiar.hijos.all()

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
        "foto_perfil",
    ]

    def form_valid(self, form):
        if "foto_perfil" in self.request.FILES:
            print("Encontramos la foto")
            # If yes, then grab it from the POST form reply
            form.instance.foto_perfil = self.request.FILES["foto_perfil"]
        usuario = self.request.user.usuario
        # Catch an instance of the object
        nino = form.save(commit=False)
        nino.save()

        familiar = models.Tutor.objects.get(usuario_id=usuario.id)
        familiar.hijos.add(nino)
        self.success_url = self.model.get_absolute_url(nino)
        return super(NinoCreate, self).form_valid(form)


class Perfil_Control_medico_View(DetailView):
    model = models.Control_medico
    context_object_name = "perfil_control_medico"
    template_name = "carnets/indexControl_medico/control_medico_detail.html"

    def get(self, request, *args, **kwargs):
        from django.http import Http404

        try:
            control_medico = get_object_or_404(models.Control_medico, pk=kwargs["pk"])
            context = {"control_medico": control_medico}
            return render(
                request,
                "carnets/indexControl_medico/control_medico_detail.html",
                context,
            )
        except Http404:
            # redirect is here
            from django.shortcuts import redirect
            from django.urls import reverse_lazy

            return redirect(reverse("carnets:crear_control_medico"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["control_medico"] = models.Control_medico.objects.get(self.object)
        return context


class Control_medico_form(forms.ModelForm):
    class Meta:
        model = models.Control_medico
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

    def _init_(self, *args, **kwargs):
        nino = kwargs.pop("nino")
        super(Control_medico_form, self)._init_(*args, **kwargs)
        self.fields["carnet"].queryset = Folder.objects.filter(carnet=nino.carnet)


class Control_medicoCreate(CreateView):
    model = models.Control_medico
    form_class = Control_medico_form
    template_name = "carnets/indexControl_medico/control_medico_form.html"

    def form_valid(self, form):
        if "foto_perfil" in self.request.FILES:
            print("Encontramos la foto")
            # If yes, then grab it from the POST form reply
            form.instance.foto_perfil = self.request.FILES["foto_perfil"]
            form.instance.usuario = self.request.user.usuario
        return super().form_valid(form)


class Control_medico_List_View(ListView):

    model = models.Control_medico
    paginate_by = 20  # if pagination is desired
    template_name = "carnets/indexControl_medico/control_medico_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Control_medico_list"] = models.Control_medico.objects.all()
        return context
