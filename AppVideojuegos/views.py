from django.shortcuts import render
from AppVideojuegos.models import Consolas
from AppVideojuegos.forms import ConsolaFormulario

# Create your views here.
def agregar_consolas(request):

    if request.method=="POST":

        #VAMOS A GUARDAR LA INFO
        info_formulario = ConsolaFormulario(request.POST)

        if info_formulario.is_valid():

            info = info_formulario.cleaned_data

            nueva_consola = Consolas(nombre=info["nombre"], empresa=info["empresa"], año=info["año"], fecha=info["fecha"])

            nueva_consola.save()

            return render(request, "todos_consolas.html")

            

    else:
        nuevo_formulario = ConsolaFormulario() #crea un formulario vacío



    return render(request, "crear_consolas.html", {"formu":nuevo_formulario})


def ver_consolas(request):

    return render(request, "todos_consolas.html")
