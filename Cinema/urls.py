"""
URL configuration for Cinema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from mainApp import views as cine_views
from Center import views as reclamo_views
from django.conf import settings
from django.views.static import serve

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', cine_views.index, name='inicio'),  
    path('ticket/<int:id_venta>/', cine_views.ticket, name='ticket'),
    path('agregar_ticket/<int:id_funcion>/', cine_views.agregar_ticket, name='agregar_ticket'),
    path('comprar/<int:id>/', cine_views.comprar, name='comprar'),

    # URLs del sistema de reclamos bajo el prefijo 'reclamos/'
    path('reclamos/', reclamo_views.inicio, name='reclamos_inicio'),  # Página principal de reclamos
    path('reclamos/registrar-reclamo/', reclamo_views.registrar_reclamo, name='registrar_reclamo'),
    path('reclamos/historial-reclamos/', reclamo_views.historial_reclamos, name='historial_reclamos'),
    path('reclamos/resolver-reclamo/<int:reclamo_id>/', reclamo_views.resolver_reclamo, name='resolver_reclamo'),
]

# Manejo de archivos estáticos en modo DEBUG
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
