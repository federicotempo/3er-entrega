from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    nombre = models.CharField(max_length = 100)

class Dias(models.Model):
    cantidad_dias = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    edad = models.IntegerField()
    documento = models.IntegerField()
    vehiculo_id = models.ForeignKey(Vehiculo, on_delete = models.SET_NULL, null = True, blank = True)
    dias_id = models.ForeignKey(Dias, on_delete = models.SET_NULL, null = True, blank = True)
