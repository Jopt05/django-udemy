from datetime import date

from django.views.generic import FormView

# Create your views here.

from .models import Prestamo
from .forms import PrestamoForm

class RegistrarPrestamo(FormView):
    template_name = "prestamo/add.html"
    form_class = PrestamoForm
    success_url = "."

    def form_valid(self, form):
        # Prestamo.objects.create(
        #     lector=form.cleaned_data["lector"],
        #     libro=form.cleaned_data["libro"],
        #     fecha_prestamo=date.today(),
        #     devuelto=False
        # )

        prestamo = Prestamo(
            lector=form.cleaned_data["lector"],
            libro=form.cleaned_data["libro"],
            fecha_prestamo=date.today(),
            devuelto=False
        )
        prestamo.save()

        # libro = form.cleaned_data["libro"]
        # libro.stock = libro.stock - 1
        # libro.save()

        return super(RegistrarPrestamo, self).form_valid(form)
