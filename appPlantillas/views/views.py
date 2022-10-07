from django.shortcuts import render
from datetime import date

# Create your views here.
def home(request):
    añoNacimiento = int(request.GET['año'])
    rango = range(0,50,2)
    fecha = date.today()
    return render(request, "home.html", {"nombre":"brian spielman",
                                         "edad":2022-añoNacimiento,
                                         "rango":rango,
                                         "fecha":fecha,
                                         "valor":False,
                                         "lista":[1,2,3],
                                         "listaNull":[]})