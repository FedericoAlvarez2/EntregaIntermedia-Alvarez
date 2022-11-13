from .models import automoviles, motos, camionetas
from django.shortcuts import render
from django.http import HttpResponse

def buscar(request):
    if request.method == "POST":
        marca = request.POST["marca"]
        
        if automoviles.objects.filter(marca_contains= marca):
            automovil = automoviles.objets.filter(marca_contains = marca)
            return render (request, "buscar.html", {"automovil": automovil})

        elif motos.objects.filter(marca_contains = marca):
            moto = motos.objects.filter(titulos_contains= marca)
            return render ( request, "buscar.html", {"moto", moto})
        
        elif camionetas.objects.filter(marca_contains = marca):
            camioneta = camionetas.objects.filter(titulos_contains= marca)
            return render ( request, "buscar.html", {"camioneta", camioneta})

        else:
            return HttpResponse("Material No Encontrado")
        
    return render(request, "buscar.html")

def insertar_automoviles(request):
    if request.method == "POST":
          auto = automoviles(marca = request.POST["marca"], modelo = request.POST["modelo"], año_de_fabricacion = request.POST["año_de_fabricacion"], kilometraje = request.POST["kilometraje"], link = request.POST["link"])
          auto.save()
          return render(request, "app/insertar_automovil.html")
    return render(request, "insertar_automovil.html")

def insertar_motos(request):
    if request.method == "POST":
          moto = motos(marca = request.POST["marca"], modelo = request.POST["modelo"], año_de_fabricacion = request.POST["año_de_fabricacion"], kilometraje = request.POST["kilometraje"], link = request.POST["link"])
          moto.save()
          return render(request, "app/insertar_moto.html")
    return render(request, "insertar_moto.html")

def insertar_camioneta(request):
    if request.method == "POST":
        chata = camionetas (marca = request.POST["marca"], modelo = request.POST["modelo"], año_de_fabricacion = request.POST["año_de_fabricacion"], kilometraje = request.POST["kilometraje"], link = request.POST["link"])
        chata.save()
        return render(request, "app/insertar_camioneta.html")
    return render(request, "insertar_camioneta")
