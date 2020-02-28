from django.contrib import admin
from . import models
from autenticacion import models as auth_models
admin.site.register(models.Control)
admin.site.register(auth_models.Usuario)
