from django.db import models
# Create your models here.
from .managers import AutorManager

class Autor(models.Model):
    nombre = models.CharField(
        max_length=50
    )
    appellidos = models.CharField(
        max_length=50
    )
    nacionalidad = models.CharField(
        max_length=30
    )
    edad = models.PositiveBigIntegerField()

    objects = AutorManager()

    def __str__(self):
        return self.nombre + '-' + self.appellidos
