from django.db import models

# Create your models here.
class Consolas(models.Model):
    nombre = models.CharField(max_length=30) #equivalente al str de Python
    empresa = models.CharField(max_length=30)
    año = models.IntegerField()
    fecha = models.DateField()