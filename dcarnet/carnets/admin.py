from django.contrib import admin
from . import models
from autenticacion import models as auth_models

admin.site.register(auth_models.Usuario)
admin.site.register(models.Persona)
admin.site.register(models.Medico)
admin.site.register(models.Control_medico)
admin.site.register(models.Carnet)
admin.site.register(models.Nino)
admin.site.register(models.Tutor)
admin.site.register(models.Tipo_de_tutor)
