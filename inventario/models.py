from django.db import models

class Imagen(models.Model):
    nombre = models.CharField(max_length=50)
    origen = models.ImageField(upload_to='photos/inventory', blank=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    precio = models.IntegerField(blank=True)
    disponible = models.BooleanField(default=True)
    imagen = models.ForeignKey(Imagen,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre
