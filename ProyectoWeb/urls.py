"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppPeliculas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", inicio, name="Inicio"),

    #URLs de los modelos creados
    path("series/", ver_serie, name="Series"),
    path("pelis/", ver_pelis, name="Peliculas"),
    path("futbol/", ver_partidos, name="Partidos de Futbol"),

    #URLs para crear nuevos datos
    path("nuevaSerie/", agregar_serie),
    path("nuevaPeli/", agregar_pelicula),

    #URLs para buscar datos
    path("buscarSerieAño/", busqueda_serie_por_año),
    path("resultadosSerie/", resultados_buscar_serie_año),
    
    #path("nuevaPeli/", agregar_pelicula),



]
