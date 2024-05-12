from django.db import models
from django.db.models import Q
import datetime

class LibroManager(models.Manager):
    """ Managers para modelo Libro """

    def listar_libros(self):
        resultado = self.all()
        return resultado
    
    def filtrar_fecha(self, fecha1, fecha2):
        resultado = self.filter(
            fecha__range=[fecha1, fecha2]
            # fecha__range=['2023-01-01', '2024-01-01']
        )
        return resultado