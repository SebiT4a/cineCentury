from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse
from mainApp.models import Funcion, Peliculas, Ventas, CarouselImage
from mainApp.forms import FormVenta
import datetime


def index(request):
    funciones = Funcion.objects.all()  # Obtiene las funciones
    carousel_images = CarouselImage.objects.all()  # Obtiene las imágenes del carrusel
    data = {
        'funciones': funciones,
        'carousel_images': carousel_images  # Agrega las imágenes al contexto
    }
    return render(request, 'index.html', data)


# En views.py
def comprar(request, id):
    # Obtén la funcion según el id
    funcion = Funcion.objects.get(id=id)
    pelicula = funcion.pelicula  # Obtenemos la película asociada
    form = FormVenta(initial={'id_funcion': id})  # Inicializamos el campo oculto

    if request.method == 'POST':
        form = FormVenta(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['entradas']

            # Validar si hay suficientes asientos disponibles
            if cantidad > funcion.asientos_disponibles:
                return render(request, 'comprar.html', {
                    'funcion': funcion,
                    'pelicula': pelicula,
                    'form': form,
                    'error': 'No hay suficientes asientos disponibles.',
                })

            # Si todo es válido, redirigir al formulario de agregar_ticket
            return redirect(reverse('agregar_ticket', args=[funcion.id]))

    return render(request, 'comprar.html', {
        'funcion': funcion,
        'pelicula': pelicula,
        'form': form,
    })


def agregar_ticket(request, id_funcion):
    funcion = get_object_or_404(Funcion, id=id_funcion)
    form = FormVenta(initial={'id_funcion': id_funcion})

    if request.method == 'POST':
        # Crear el formulario con los datos POST
        form = FormVenta(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['entradas']
            codigo_descuento = form.cleaned_data.get('codigo', '').upper()

            # Validar si hay suficientes asientos disponibles
            if cantidad > funcion.asientos_disponibles:
                return render(request, 'agregar_ticket.html', {
                    'funcion': funcion,
                    'form': form,
                    'error': 'No hay suficientes asientos disponibles.',
                })

            # Actualizar los asientos
            funcion.asientos_disponibles -= cantidad
            funcion.save()

            # Crear una nueva venta sin asignar la funcion aún
            venta = Ventas(
                cliente=form.cleaned_data['cliente'],
                email=form.cleaned_data['email'],
                entradas=cantidad,
                codigo_descuento=codigo_descuento,
                fecha=datetime.date.today()
            )

            # Asignar la funcion después de crear el objeto
            venta.funcion = funcion

            # Calcular los totales
            valor_entrada = funcion.precio
            total_original = cantidad * valor_entrada
            descuento = 0
            if codigo_descuento == "INACAP":
                descuento = total_original * 0.15
            total_final = total_original - descuento

            venta.total_original = total_original
            venta.total_final = total_final
            venta.save()

            # Redirigir a la página del ticket
            return redirect(reverse('ticket', args=[venta.id]))

    return render(request, 'agregar_ticket.html', {
        'funcion': funcion,
        'form': form,
    })


def ticket(request, id_venta):
    venta = get_object_or_404(Ventas, id=id_venta)
    descuento = 0
    if venta.codigo_descuento and venta.codigo_descuento.upper() == "INACAP":
        descuento = venta.total_original * 0.15 
    return render(request, 'ticket.html', {'venta': venta, 'descuento': descuento})