from django.shortcuts import render
from AppPeliculas.models import Serie, Pelicula
from django.http import HttpResponse

# Create your views here.

def ver_serie(request):

    mis_series = Serie.objects.all() #obtener todos los datos en mi tabla Serie

    info = {"series":mis_series}

    return render(request, "AppPeliculas/series.html", info)

def inicio(request):

    return render(request, "AppPeliculas/inicio.html")





"""

def agregar_serie(request):
    
    serie1 = Serie(nombre="The 100", año=2014, temporadas=7) #Crear un objeto usando el modelo
    serie1.save()

    return HttpResponse("Se agregó una serie...")

def agregar_pelicula(request):
    
    pelicula1 = Pelicula(nombre="La La Land", año=2017, director="Damien Chazelle", 
                         genero="Musical", duracion=1.50) #Crear un objeto usando el modelo
    pelicula1.save()

    return HttpResponse("Se agregó una pelicula...")
"""