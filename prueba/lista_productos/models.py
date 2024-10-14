from django.db import models

# Create your models here.
class Producto(models.Model):
    nobre = models.TextField(max_length=40)
    descripcion = models.TextField(max_length=255)