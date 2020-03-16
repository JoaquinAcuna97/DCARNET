from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# from django.core.urlresolvers import reverse
# Create your models here.
class Usuario(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.deletion.CASCADE)

    # Add any additional attributes you want
    tipos = (
        ("a", "Familiar"),
        ("b", "Doctor"),
    )
    tipo_usuario = models.CharField(max_length=1, choices=tipos)

    # pip install pillow to use this!
    # Optional: pip install pillow --global-option=”build_ext” --global-option=”--disable-jpeg”
    foto_perfil = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
