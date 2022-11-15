from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class Produccion(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits = 5, decimal_places = 2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=20)

    def __str__(self):
        return self.producto

class Produccin(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=20)

    def __str__(self):
        return self.producto

class materiaprima(models.Model):
    cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)
    proveedor = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=20)

    def __str__(self):
        return self.proveedor

class Inventario(models.Model):
    descripcion = models.CharField(max_length=100)
    stock = models.PositiveIntegerField()
    entrada = models.PositiveIntegerField()
    salida = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits = 7, decimal_places = 2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

class Entrada(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=20)

    def __str__(self):
        return self.producto

class Salida(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=20)

    def __str__(self):
        return self.producto