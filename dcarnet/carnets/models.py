from django.db import models
from autenticacion import models as authmodels
from django.utils import timezone
from django.urls import reverse

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
    fecha_de_creacion = timezone.now()

    def get_absolute_url(self):
        return reverse("detail_medico", kwargs={"pk": self.pk})


class Control_medico(models.Model):
    edad = models.IntegerField()
    peso = models.FloatField()
    talla = models.FloatField()
    pd = models.FloatField()
    alimentacion = models.CharField(max_length=200)
    hierro = models.FloatField()
    vit_D = models.FloatField()
    observaciones = models.TextField()
    presion_arterial = models.FloatField()
    proximo_control = models.DateField()
    fecha_de_creacion = timezone.now()

    def __str__(self):
        return "Control medico Ninio" + self.ninio + " fecha: " + self.fecha_de_creacion


class Carnet(models.Model):
    # campos adicicionales: ultimo control, graficas, etc
    control_medico = models.ForeignKey(
        Control_medico, blank=True, null=True, on_delete=models.SET_NULL
    )


class Nino(Persona):
    servicio_de_salud = models.CharField(max_length=200)
    carnet = models.OneToOneField(
        Carnet, blank=True, null=True, on_delete=models.CASCADE
    )
    medico_asignado = models.ForeignKey(
        Medico, blank=True, null=True, on_delete=models.SET_NULL
    )


class Agenda(models.Model):
    medico_asignado = models.OneToOneField(
        Medico, blank=True, null=True, on_delete=models.SET_NULL
    )
    fecha_control = models.DateField()
    nino = models.ForeignKey(Nino, blank=True, null=True, on_delete=models.SET_NULL)
    control_medico = models.OneToOneField(
        Control_medico, blank=True, null=True, on_delete=models.SET_NULL
    )


class Tutor(Persona):
    hijos = models.ManyToManyField(Nino, blank=True, null=True, through="Tipo_de_tutor")
    agenda = models.ForeignKey(Agenda, blank=True, null=True, on_delete=models.SET_NULL)
    usuario = models.OneToOneField(authmodels.Usuario, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("detail_familiar", kwargs={"pk": self.pk})


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
