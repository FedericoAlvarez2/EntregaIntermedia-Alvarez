from appentrega import views
from django.urls import path
from appentrega.views import *


urlpatterns = [
    path ("buscar/", buscar, name="buscar"),
    path("insertar_automoviles/", insertar_automoviles, name= "insertar-automoviles"),
    path("insertar_motos/", insertar_motos, name= "insertar-motos"),
    path("insertar_camioneta/", insertar_camioneta, name= "insertar-camioneta"),
]