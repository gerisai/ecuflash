from django.shortcuts import render

from .models import Producto
from .choices import make_choices

def index(request):
    productos = Producto.objects.order_by('-nombre').filter(disponible=True)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            productos = productos.filter(nombre__icontains=keywords)

    if 'marca' in request.GET:
        marca = request.GET['marca']
        if marca:
            productos = productos.filter(marca__iexact=marca)

    if 'modelo' in request.GET:
        modelo = request.GET['modelo']
        if modelo:
            productos = productos.filter(modelo__icontains=modelo)
    
    if 'anio' in request.GET:
        año = request.GET['anio']
        if año:
            productos = productos.filter(año__iexact=año)

    context = {
        'productos': productos,
        'values': request.GET,
        'marcas': make_choices
    }

    return render(request,'inventory/list.html', context)