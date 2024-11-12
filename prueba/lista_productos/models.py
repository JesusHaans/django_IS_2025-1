from django.db import models

# Create your models here.
class Producto(models.Model):
    nobre = models.TextField(max_length=40)
    descripcion = models.TextField(max_length=255)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{" + self.nobre + "}" + ":" + self.descripcion + "de" + self.proveedor.nombre

class Proveedor(models.Model):
    nombre = models.TextField(max_length=40)
    direccion = models.TextField(max_length=255)
    telefono = models.TextField(max_length=20)

    def __str__(self):
        return "{" + self.nombre + "}" + ":" + self.direccion + ":" + self.telefono
    
class renta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    numero = models.IntegerField()
    categoria = models.TextField(max_length=40)

    def __str__(self):
        return "{" + str(self.fecha) + "}" + ":" + str(self.numero) + ":" + self.categoria