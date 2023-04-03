from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    def __str__(self) -> str:
        return f"id = {self.nombre}"

class Habilidades(models.Model):
    nombre =  models.CharField(max_length=50)
class Empleado(models.Model):
    #Clave foranea
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Habilidades = models.ManyToManyField(Habilidades) #Varias habilidades
    nombre  =  models.CharField(max_length=40)
    fecha_de_nacimiento = models.CharField(max_length=40)
    antiguedad = models.IntegerField(default=0)