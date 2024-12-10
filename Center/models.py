from django.db import models

class Reclamo(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    email = models.EmailField()
    titulo_pelicula = models.CharField(max_length=200)
    texto_reclamo = models.TextField()
    fecha_reclamo = models.DateTimeField(auto_now_add=True)
    resuelto = models.BooleanField(default=False)