from django.shortcuts import render, get_object_or_404

from inicio.models import *

def index(request):
	articulos = Articulo.objects.all()
	return render(request, 'index.html', locals())

def detail(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)
    return render(request, 'hola.html', {'articulo': articulo})


