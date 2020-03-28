from django.db import models
from autenticacion import models as authmodels
from django.utils import timezone
from django.urls import reverse
from django import forms


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_de_nacimiento = models.DateTimeField(blank=True, null=True)
    fecha_de_creacion = models.DateTimeField(default=timezone.now)
    documento_de_Identidad = models.CharField(max_length=200)
    lugar_de_nacimiento = models.CharField(max_length=200)

    # Add any additional attributes you want
    tipos = (
        ("a", "Tutor"),
        ("b", "Doctor"),
        ("c", "Nino"),
    )
    tipo_persona = models.CharField(max_length=1, choices=tipos)

    def __str__(self):
        return self.nombre + " " + self.apellido


class Medico(Persona):
    especializacion = (
        ("Aler.", "Alergología"),
        ("Anes.", "Anestesiología"),
        ("Card.", "Cardiología"),
        ("Gast.", "Gastroenterología"),
        ("Endo.", "Endocrinología"),
        ("Geri.", "Geriatría"),
        ("Hema.", "Hematología"),
        ("Infe.", "Infectología"),
        ("Aeroes", "Medicina aeroespacial"),
        ("Depo", "Medicina del deporte"),
        ("Traba", "Medicina del trabajo"),
        ("Urgenc", "Medicina de urgencias"),
        ("Famili", "Medicina familiar y comunitaria"),
        ("Física", "Medicina física y rehabilitación"),
        ("Intens", "Medicina intensiva"),
        ("Intern", "Medicina interna"),
        ("Forens", "Medicina forense"),
        ("Preventiva.", "Medicina preventiva y salud pública"),
        ("Nefr.", "Nefrología"),
        ("Neum.", "Neumología"),
        ("Neur.", "Neurología"),
        ("Nutr.", "Nutriología"),
        ("Onco.", "Oncología médica"),
        ("Onco.", "Oncología radioterápica"),
        ("Pedi.", "Pediatría"),
        ("Psiq.", "Psiquiatría"),
        ("Reum.", "Reumatología"),
        ("Toxi.", "Toxicología"),
    )
    usuario = models.OneToOneField(authmodels.Usuario, on_delete=models.CASCADE)
    tipo_especializacion = models.CharField(max_length=11, choices=especializacion)

    def get_absolute_url(self):
        return reverse("carnets:detail_medico", kwargs={"pk": self.pk})


class Carnet(models.Model):
    fecha_de_creacion = models.DateTimeField(default=timezone.now)
    # campos adicicionales: ultimo control, graficas, etc

    @classmethod
    def create(cls):
        carnet = cls()
        # do something with the book
        return carnet

class Control_medico(models.Model):
    edad = models.IntegerField()
    peso = models.FloatField()
    talla = models.FloatField()
    pd = models.FloatField()
    alimentacion = models.CharField(max_length=200)
    hierro = models.CharField(max_length=30)
    vit_D = models.CharField(max_length=30)
    observaciones = models.TextField()
    presion_arterial = models.FloatField()
    proximo_control = models.DateField()
    fecha_de_creacion = models.DateTimeField(default=timezone.now)
    carnet = models.ForeignKey(
        Carnet, blank=True, null=True, on_delete=models.SET_NULL
    )
    def __str__(self):
        return "Control medico Ninio" + " fecha: " + str(self.fecha_de_creacion)

    def get_absolute_url(self):
        return reverse("carnets:detail_Control_medico", kwargs={"pk": self.pk})




class Nino(Persona):
    servicio_de_salud = models.CharField(max_length=200)
    carnet = models.OneToOneField(
        Carnet, blank=True, null=True, on_delete=models.CASCADE
    )
    medico_asignado = models.ForeignKey(
        Medico, blank=True, null=True, on_delete=models.SET_NULL
    )
    foto_perfil = models.ImageField(upload_to="profile_pics", blank=True)

    def get_absolute_url(self):
        return reverse("carnets:detail_nino", kwargs={"pk": self.pk})


class Tutor(Persona):
    hijos = models.ManyToManyField(Nino, blank=True, null=True, through="Tipo_de_tutor")
    usuario = models.OneToOneField(authmodels.Usuario, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("carnets:detail_familiar", kwargs={"pk": self.usuario.pk})


class Tipo_de_tutor(models.Model):
    nino = models.ForeignKey(Nino, blank=True, null=True, on_delete=models.SET_NULL)
    tutor = models.ForeignKey(Tutor, blank=True, null=True, on_delete=models.SET_NULL)
    tipo_de_tutor = models.CharField(max_length=64)

    def __str__(self):
        return (
            "Tutor: "
            + self.tutor
            + " tipo de relacion: "
            + self.tipo_de_relacion
            + " Niño: "
            + self.Nino
        )
