from django.db import models

class consolas(models.Model):
    imagen = models.ImageField(upload_to='consolas_img/', null=True, blank=True)
    modelo = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    precio = models.IntegerField()
    fecha_de_creacion = models.DateField()

    def __str__(self):
        return f"{self.modelo} by {self.empresa}, Created: {self.fecha_de_creacion} -- ${self.precio}"


class accesorios(models.Model):
    producto = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    duracion_bateria = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.producto} by {self.empresa}, Bateria: {self.duracion_bateria} Horas -- ${self.precio}"


class juegos(models.Model):
    juego = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.juego} by {self.empresa}, Categoria: {self.categoria} -- ${self.precio}"
