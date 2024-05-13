from django.contrib import admin

# Register your models here.
from .models import Empleado, Cliente

admin.site.register(Empleado)
admin.site.register(Cliente)