from django.db import models


class Peliculas(models.Model):
    nombre = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    anno = models.PositiveIntegerField()
    duracion = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="peliculas")
    descripcion = models.TextField(null=True, blank=True)  # Campo para la descripción
    trailer_url = models.URLField(blank=True, null=True)  # URL del tráiler
    imagen_trailer = models.ImageField(upload_to="trailers", blank=True, null=True)  # Imagen del tráiler

    def __str__(self):
        return self.nombre + " (" + str(self.anno) + ")"

    
    
class Funcion(models.Model):
    pelicula = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    precio = models.PositiveIntegerField()
    asientos_disponibles = models.PositiveIntegerField()
    asientos_vendidos = models.PositiveIntegerField()
    sala = models.CharField(max_length=50)

    def __str__(self):
        return self.pelicula.nombre


class Ventas(models.Model):
    cliente = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    entradas = models.PositiveIntegerField()
    precio_entrada = models.PositiveIntegerField(default=5000)
    codigo_descuento = models.CharField(max_length=20, blank=True, null=True)  # Campo para el código de descuento
    total_original = models.PositiveIntegerField(default=0, editable=False)
    total_final = models.PositiveIntegerField(default=0, editable=False)
    fecha = models.DateField(auto_now_add=True)

    def calcular_totales(self):
        self.total_original = self.entradas * self.precio_entrada
        descuento = 0
        if self.codigo_descuento and self.codigo_descuento.upper() == "INACAP":  # Verifica el código de descuento
            descuento = self.total_original * 0.15
        self.total_final = self.total_original - descuento

    def save(self, *args, **kwargs):
        self.calcular_totales()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venta de {self.cliente} - {self.funcion}"
    

    
class CarouselImage(models.Model):
    title = models.CharField(max_length=100, help_text="Título de la imagen")
    description = models.TextField(blank=True, help_text="Descripción corta (opcional)")
    image = models.ImageField(upload_to='carousel/', help_text="Sube la imagen para el carrusel")
    order = models.PositiveIntegerField(default=0, help_text="Orden de la imagen en el carrusel")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title