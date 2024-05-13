from django.db import models
# Create your models here.
from .managers import AutorManager

class Persona(models.Model):
    nombres = models.CharField(
        max_length=50
    )
    apellidos = models.CharField(
        max_length=50
    )
    nacionalidad = models.CharField(
        max_length=50
    )
    edad = models.PositiveBigIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.nombres + '-' + self.apellidos

class Autor(Persona):

    pseudonimo = models.CharField(
        'pseudonimo',
        max_length=50,
        blank=True
    )

    objects = AutorManager()
