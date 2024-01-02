from django.db import models

# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    director = models.CharField(max_length=40)
    genero = models.CharField(max_length=30)
    duracion = models.FloatField()
    
class Serie(models.Model):
    nombre = models.CharField(max_length=40)
    año = models.IntegerField()
    temporadas = models.IntegerField()

class Futbol(models.Model):
    equipo_local = models.CharField(max_length=40)
    equipo_visitante = models.CharField(max_length=40)
    resultado = models.CharField(max_length=40)
    fecha = models.DateField()

