from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from datetime import date
from appPlantillas.models import *

# Create your views here.
def home(request):
    añoNacimiento = int(request.GET['año'])
    rango = range(0,50,2)
    fecha = date.today()
    
    return render(request, "home.html", {"nombre":"brian spielsfsdfwern",
                                         "edad":2022-añoNacimiento,
                                         "rango":rango,
                                         "fecha":fecha,
                                         "valor":False,
                                         "lista":[1,2,3],
                                         "listaNull":[]},status=200)

def inicial(request,rut,nombre):
    yo = Persona()
    yo.rut = rut
    yo.nombre = nombre.upper()
    if request.method == 'GET':
        try:
            variable = request.GET["elemento"]
        except Exception:
            variable = "NO SE PASO NINGUN ELEMENTO"
    elif request.method == 'POST':
        variable = request.POST["elemento"]
    return render(request, "persona.html", {"persona":yo,"texto":variable},status=500)

def inicial2(request,rut,nombre,nacionalidad):
    yo = Persona()
    yo.rut = rut
    yo.nombre = nombre
    
    return render(request, "persona.html", {"persona":yo,"pais":nacionalidad,"text":request.GET["elemento"]},)

def solicitudRespuesta(request):
    if request.method == 'GET':
        return HttpResponse("<h1>Todo Ok, realizaste un GET</h1>")
    elif request.method == 'POST':
        return HttpResponse("<h1>Todo Ok, realizaste un POST</h1>")