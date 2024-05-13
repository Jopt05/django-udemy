from django.db import models

# Create your models here.

class Persona(models.Model):

    full_name = models.CharField(
        'nombres',
        max_length=50
    )
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField(
        'Pasaporte',
        max_length=50
    )
    edad = models.PositiveIntegerField()
    apelativo = models.CharField('Apelativo', max_length=10)

    class Meta:
        # verbose_name = "Persona"
        # verbose_name_plural = "Personas"
        # Nombre de tabla 
        # db_table = "persona"
        # Combinacion de valores unicos, una combinación de ambos más de una vez es imposible
        unique_together = ['pais', 'apelativo']
        
        # constraints = [
        #     models.CheckConstraint(
        #         check=models.Q(edad__gte=18), 
        #         name="edad_mayor_18"
        #     )
        # ]

        abstract = True

    def __str__(self) -> str:
        return self.full_name
    
class Empleado(Persona):
    empleo = models.CharField(
        max_length=50
    )

class Cliente(Persona):
    email = models.EmailField('email')