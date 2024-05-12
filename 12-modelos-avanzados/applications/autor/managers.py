from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """ Managers para modelo Autor """

    def listar_autores(self):
        return self.all()
    
    def buscar_autor(self, palabra_clave):
        resultado = self.filter(
            nombre__icontains=palabra_clave
        ).order_by(
            'appellidos',
            'nombre'
        )
        return resultado
    
    def buscar_autor2(self, palabra_clave):
        resultado = self.filter(
            Q(nombre__icontains=palabra_clave) |
            Q(appellidos__icontains=palabra_clave)
        )
        return resultado
    
    def buscar_autor_exclude(self, palabra_clave):
        resultado = self.filter(
            nombre__icontains=palabra_clave
        ).exclude(
            edad=70
        )
        return resultado
    
    def buscar_autor_edad(self, edad):
        resultado = self.filter(
            edad__gt=edad
        )
        return resultado