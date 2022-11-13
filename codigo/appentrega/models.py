from django.db import models

class automoviles(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año_de_fabricacion= models.CharField(max_length= 100)
    kilometraje = models.CharField(max_length= 50)

class motos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año_de_fabricacion= models.CharField(max_length= 100)
    kilometraje = models.CharField(max_length= 50)

class camionetas(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año_de_fabricacion= models.CharField(max_length= 100)
    kilometraje = models.CharField(max_length= 50)


