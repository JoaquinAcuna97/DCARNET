from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse
from django_countries.fields import CountryField

# Create your models here.
class Usuario(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User,on_delete=models.deletion.CASCADE)

    # Add any additional attributes you want
    tipos = (
        ('a', 'Familiar'),
        ('b', 'Doctor'),
    )
    tipo_usuario = models.CharField(max_length=1, choices=tipos)

    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    foto_perfil = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_de_nacimiento = models.DateTimeField(blank=True, null=True)
    fecha_de_creacion = models.DateTimeField(default=timezone.now)
    documento_de_Identidad = models.CharField()
    lugar_de_nacimiento = modelsCountryField()

   # Add any additional attributes you want
    tipos = (
        ('a', 'Tutor'),
        ('b', 'Doctor'),
        ('c', 'niño'),
    )
    tipo_usuario = models.CharField(max_length=1, choices=tipos)


    def __str__(self):
        return self.nombre+' '+self.apellido


class Niño(Persona):
    servicio_de_salud = models.CharField()
    numero_de_historia_clinica =
    medico_asignado = models.ForeignKey(Medico, on_delete=models.CASCADE)


class Tipo_de_relacion(models.Model):
    niño = models.ForeignKey(Niño, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    tipo_de_relacion = models.CharField(max_length=64)

    def __str__(self):
        return self.tutor+' tipo de relacion: '+self.tipo_de_relacion+self.niño


class Tutor(Persona):
    hijos = models.ManyToManyField(Niño, through='Tipo_de_relacion')
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)


class Agenda(models.model):
    medico_asignado = models.OneToOneField(Medico, on_delete=models.CASCADE)
    fecha_control = models.DateField()
    niño = models.ForeignKey(Niño, on_delete=models.CASCADE)
    tutor = models.OneToOneField(Tutor, on_delete=models.SET_NULL)
    control_medico = models.OneToOneField(Control_medico, on_delete=models.SET_NULL)


class Medico(Persona):

    especializacion = (
        ('Aler.', 'Alergología'),
        ('Anes.', 'Anestesiología'),
        ('Card.', 'Cardiología'),
        ('Gast.', 'Gastroenterología'),
        ('Endo.', 'Endocrinología'),
        ('Geri.', 'Geriatría'),
        ('Hema.', 'Hematología'),
        ('Infe.', 'Infectología'),
        ('Aeroes', 'Medicina aeroespacial'),
        ('Depo', 'Medicina del deporte'),
        ('Traba', 'Medicina del trabajo'),
        ('Urgenc', 'Medicina de urgencias'),
        ('Famili', 'Medicina familiar y comunitaria'),
        ('Física', 'Medicina física y rehabilitación'),
        ('Intens', 'Medicina intensiva'),
        ('Intern', 'Medicina interna'),
        ('Forens', 'Medicina forense'),
        ('Preventiva.', 'Medicina preventiva y salud pública'),
        ('Nefr.', 'Nefrología'),
        ('Neum.', 'Neumología'),
        ('Neur.', 'Neurología'),
        ('Nutr.', 'Nutriología'),
        ('Onco.', 'Oncología médica'),
        ('Onco.', 'Oncología radioterápica'),
        ('Pedi.', 'Pediatría'),
        ('Psiq.', 'Psiquiatría'),
        ('Reum.', 'Reumatología'),
        ('Toxi.', 'Toxicología'),
    )
    tipo_especializacion = models.ChoiceField(max_length=1, choices=especializacion)


class Control_medico()
    niño = models.ForeignKey(Niño, on_delete=models.CASCADE)
    edad = models.IntegerField()
    peso = models.FloatField()
    talla = models.FloatField()
    pd = models.FloatField()
    alimentacion = models.CharField()
    hierro = models.FloatField()
    vit_D = models.FloatField()
    observaciones = models.TextField()
    presion_arterial = models.FloatField()
    proximo_control = models.DateField()

