from django.contrib import admin
from .models import Empleado, Departamento, Habilidades


# Register your models here.
admin.site.register(Empleado)
admin.site.register(Departamento)
admin.site.register(Habilidades)