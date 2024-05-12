from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.generic import ListView

from .models import Autor

class ListAutores(ListView):
    model = Autor
    context_object_name = 'lista_autores'
    template_name = 'autor/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", "")
        if palabra_clave:
            return Autor.objects.buscar_autor(palabra_clave) 
        return Autor.objects.listar_autores()