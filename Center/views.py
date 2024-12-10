from django.shortcuts import render, redirect
from Center.models import Reclamo

def inicio(request):
    return render(request, 'base.html')

def registrar_reclamo(request):
    if request.method == 'POST':
        nombre_cliente = request.POST['nombre_cliente']
        email = request.POST['email']
        titulo_pelicula = request.POST['titulo_pelicula']
        texto_reclamo = request.POST['texto_reclamo']
        
        reclamo = Reclamo.objects.create(
            nombre_cliente=nombre_cliente,
            email=email,
            titulo_pelicula=titulo_pelicula,
            texto_reclamo=texto_reclamo
        )
        reclamo.save()
        return redirect('historial_reclamos')
    return render(request, 'registrar_reclamo.html')

def historial_reclamos(request):
    reclamos = Reclamo.objects.all()
    return render(request, 'historial_reclamos.html', {'reclamos': reclamos})

def resolver_reclamo(request, reclamo_id):
    reclamo = Reclamo.objects.get(id=reclamo_id)
    reclamo.resuelto = True
    reclamo.save()
    return redirect('historial_reclamos')