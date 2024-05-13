from django.db import models
from django.db.models import Q, Count
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
    
    def listar_libros_categoria(self, id_categoria):
        return self.filter(
            # Esto es un id
            categoria__id=id_categoria
        ).order_by(
            'titulo'
        )
    
    def agregar_autor_libro(self, libro_id, autor_id):
        libro = self.get(id=libro_id)
        libro.autores.add(autor_id)
        return libro
    
    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )
        return resultado
    
    def num_libros_prestados(self):
        resultado = self.annotate(
            num_prestados=Count('libro_prestamo')
        )

        for r in resultado:
            print("======")
            print(r, r.num_prestados)

        return resultado
    
class CategoriaManager(models.Manager):

    def categoria_por_autor(self, autor_id):
        return self.filter(
            categoria_libro__autores__id=autor_id  
            # Quiero consultas que no se repitan
        ).distinct()
    
    def listar_categoria_libros(self):
        resultado = self.annotate(
            numero_libros=Count('categoria_libro')
        )

        for r in resultado:
            print("++++")
            print(r, r.numero_libros)

        return resultado