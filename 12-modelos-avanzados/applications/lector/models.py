from django.db import models

from applications.libro.models import Libro
from applications.autor.models import Persona
from .managers import PrestamoManager

# Create your models here.

class Lector(Persona):

    def __str__(self):
        return self.nombres
    
class Prestamo(models.Model):
    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE
    )
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name='libro_prestamo'
    )
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(
        blank=True,
        null=True
    )
    devuelto = models.BooleanField()

    def save(self, *args, **kwargs):
        self.libro.stock = self.libro.stock - 1
        self.libro.save()
        super(Prestamo, self).save(*args, **kwargs)

    objects = PrestamoManager()

    def __str__(self) -> str:
        return self.libro.titulo