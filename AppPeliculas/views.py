from django.shortcuts import render
from AppPeliculas.models import Serie, Pelicula
from AppPeliculas.forms import SerieFormulario, PeliculaFormulario
from django.http import HttpResponse

# Create your views here.

def inicio(request):

    return render(request, "AppPeliculas/inicio.html")

def ver_serie(request):

    mis_series = Serie.objects.all() #obtener todos los datos en mi tabla Serie

    info = {"series":mis_series}

    return render(request, "AppPeliculas/series.html", info)

def ver_pelis(request):

    return render(request, "AppPeliculas/peliculas.html")

def ver_partidos(request):

    return render(request, "AppPeliculas/partidos.html")



def agregar_serie(request):
    
    #Depende de darle click al botón enviar o guardar

    if request.method == "POST":

        nuevo_formulario = SerieFormulario(request.POST) #obtener los datos del formulario HTML

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data #para tenerlos en modo diccionario

            serie_nueva = Serie(nombre=info["nombre"], año=info["año"], temporadas=info["temporadas"])

            serie_nueva.save()

            return render(request, "AppPeliculas/inicio.html") #muestrame la plantilla de inicio luego de guardar la info!!!
    
    else: #si la persona no la ha hecho click al botón enviar

        nuevo_formulario  = SerieFormulario() #mostraremos un formulario vacio

    return render(request, "AppPeliculas/formu_serie.html", {"mi_formu":nuevo_formulario})



def agregar_pelicula(request):
    
    #Depende de darle click al botón enviar o guardar

    if request.method == "POST":

        nuevo_formulario = PeliculaFormulario(request.POST) #obtener los datos del formulario HTML

        if nuevo_formulario.is_valid():

            info = nuevo_formulario.cleaned_data #para tenerlos en modo diccionario

            peli_nueva = Pelicula(nombre=info["nombre"], año=info["año"], director=info["director"],
                                  genero=info["genero"], duracion=info["duracion"])

            peli_nueva.save()

            return render(request, "AppPeliculas/inicio.html") #muestrame la plantilla de inicio luego de guardar la info!!!
    
    else: #si la persona no la ha hecho click al botón enviar

        nuevo_formulario  = PeliculaFormulario() #mostraremos un formulario vacio

    return render(request, "AppPeliculas/formu_peli.html", {"mi_formu":nuevo_formulario})


def busqueda_serie_por_año(request):

    return render(request, "AppPeliculas/buscar_serie_año.html")


def resultados_buscar_serie_año(request):

    if request.method=="GET":

        año_pedido = request.GET["año"]
        resultados_series = Serie.objects.filter(año__icontains=año_pedido)


        return render(request, "AppPeliculas/buscar_serie_año.html", {"series":resultados_series})

    else:
        return render(request, "AppPeliculas/buscar_serie_año.html")


"""

def agregar_serie_con_html(request):

    #saber que el usuario ha dado click en el botón del formulario
    if request.method == "POST":

        serie_nueva = Serie(
            nombre = request.POST["name"], 
            año = request.POST["year"], 
            temporadas = request.POST["seasons"]
            )

        serie_nueva.save()

    return render(request, "AppPeliculas/nueva_serie.html")
    


def agregar_pelicula(request):
    
    pelicula1 = Pelicula(nombre="La La Land", año=2017, director="Damien Chazelle", 
                         genero="Musical", duracion=1.50) #Crear un objeto usando el modelo
    pelicula1.save()

    return HttpResponse("Se agregó una pelicula...")
"""