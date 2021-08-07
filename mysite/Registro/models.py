from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Cliente(models.Model):

    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    email = models.EmailField()
    contraseña = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nombre


class Producto(models.Model):

    nombre_producto = models.CharField(max_length=20)
    precio = models.FloatField()
    categoria = models.CharField(max_length=15)


class Factura(models.Model):

    numero_factura = models.IntegerField(primary_key=True)
    id_cliente = ForeignKey(Cliente, on_delete=CASCADE)
    id_produto = ForeignKey(Producto, on_delete=CASCADE)
    fecha = models.DateTimeField()
