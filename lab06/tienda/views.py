from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto

# Create your views here.

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    cat_list = Categoria.objects.order_by('nombre')
    context = {'product_list': product_list, 'cat_list': cat_list}
    return render(request, 'tienda/index.html', context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'tienda/producto.html', {'producto': producto})

def categoria(request, categoria_id):
    product_list = Producto.objects.filter(categoria = categoria_id)[:6]
    cat_list = Categoria.objects.order_by('nombre')
    context = {'product_list': product_list, 'cat_list': cat_list}
    return render(request, 'tienda/categoria.html', context)