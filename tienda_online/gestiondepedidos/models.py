from django.db import models

# Create your models here.

class Clientes (models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=15)

    def __str__(self) -> str:
        return (f"{self.nombre} {self.apellido} {self.telefono}")

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    categoria=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self) -> str:
        return (f"El articulo {self.nombre} correspondiente a {self.categoria} tiene un precio de ${self.precio}")

class Pedidos(models.Model):
    numero=models.IntegerField(null=True)
    fecha=models.DateField()
    entregado=models.BooleanField()

    def __str__(self) -> str:
        if self.entregado == True: 
            self.entregado= "Fue entregado" 
        else:
            self.entregado = "No fue entregado"
        return (f"El pedido n°{self.numero} realizado el dia {self.fecha}.{self.entregado}")

