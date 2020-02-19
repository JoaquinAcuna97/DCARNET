from django.db import models

class Control(models.Model):
    created_at= models.DateField()
    edad= models.CharField(max_length=3)
    peso= models.CharField(max_length=3)
    talla= models.CharField(max_length=3)
    pd = models.CharField(max_length=3)
    hierro= models.CharField(max_length=3)
    observaciones= models.TextField()
    proximocontrol= models.DateTimeField()

    def __str__(self):
        return self.edad
