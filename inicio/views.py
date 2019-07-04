from django.shortcuts import render, get_object_or_404

from inicio.models import *


def index(request):
	articuloimagen = Articulo.objects.all().prefetch_related('imagenes_articulos')
	'''for articulo in articuloimagen:
		print(articulo.nombre)
		print(articulo.precio)
		algo = articulo.imagenes_articulos.all().first()
		for imagen in articulo.imagenes_articulos.all():
			print(imagen.foto)'''
	return render(request, 'index.html', locals())

def detail(request, articulo_id):
    articulo = get_object_or_404(Articulo, pk=articulo_id)

    #imagenes = get_object_or_404(ArticuloImagen, articulo_id=articulo_id)
    qs = ArticuloImagen.objects.filter(articulo_id=articulo_id)
    return render(request, 'detail.html', locals())
    
    #return render(request, 'hola.html', {'articulo': articulo, 'imagenes': imagenes[0]})


