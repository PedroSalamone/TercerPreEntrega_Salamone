from django.db import models

# Create your models here.
from django.db import models

class Paciente(models.Model):
    apellido = models.CharField(max_length=20)
    trabajo = models.CharField(max_length=30)
    cant_piezas = models.IntegerField()
    color = models.IntegerField()

class Odontologo(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)

class Entregas(models.Model):
    fecha_ent = models.DateField()
    fecha_sal = models.DateField()
    entregado = models.BooleanField()

class Valor(models.Model):
    precio = models.IntegerField()
    mes_fact = models.DateField()