from django.views.generic import ListView

from .models import Libro

class ListLibros(ListView):
    model = Libro
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        fecha1 = self.request.GET.get('fecha1', '')
        fecha2 = self.request.GET.get('fecha2', '')
        if fecha1 and fecha2:
            return Libro.objects.filtrar_fecha(fecha1, fecha2)
        return Libro.objects.listar_libros()