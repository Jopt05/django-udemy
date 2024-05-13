from django.db.models import Q, Count, Avg
from django.db.models.functions import Lower
from django.db import models

class PrestamoManager(models.Manager):
    """  Procedimientos para préstamo """

    def libros_promedio_edades(self):
        resultado = self.filter(
            # Libro de it
            libro__id='1'
        ).aggregate(
            promedio_edad=Avg(
                'lector__edad'
            )
        )
        return resultado
    
    def num_libros_prestados(self):
        resultado = self.values(
            # Un prestamo puede tener solo un libro
            'libro'
        ).annotate(
            # Por cada libro va a contar entonces, cuantas veces esta ese id en prestamos
            num_prestados=Count('libro'),
            titulo=Lower('libro__titulo')
        )

        for r in resultado:
            print("======")
            print(r, r['num_prestados'])

        return resultado