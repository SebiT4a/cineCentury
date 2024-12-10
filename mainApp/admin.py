from django.contrib import admin
from mainApp.models import Peliculas, Funcion, CarouselImage

# Configuración personalizada para el modelo Peliculas
@admin.register(Peliculas)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'anno', 'director', 'duracion', 'descripcion', 'trailer_url', 'imagen_trailer']
    fieldsets = (
        (None, {
            'fields': ('nombre', 'director', 'anno', 'duracion', 'imagen', 'descripcion', 'trailer_url', 'imagen_trailer')
        }),
    )
    search_fields = ['nombre', 'director']  # Agrega barra de búsqueda por nombre y director
    list_filter = ['anno']  # Agrega filtro lateral por año

# Configuración personalizada para el modelo Funcion
@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ['pelicula', 'fecha', 'hora', 'asientos_vendidos', 'sala']
    list_filter = ['fecha', 'sala']  # Filtrar funciones por fecha y sala
    search_fields = ['pelicula__nombre']  # Búsqueda por nombre de película

# Configuración personalizada para el modelo CarouselImage
@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'image')
    list_editable = ('order',)  # Permite editar el orden directamente en la lista de elementos
    search_fields = ('title',)  # Agrega barra de búsqueda por título
    list_filter = ('order',)  # Agrega filtro lateral por orden
