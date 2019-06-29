from django.db import models

from django.conf import settings

class Foto(models.Model):
	nombre_foto = models.CharField(max_length=100, blank=True)
	foto = models.ImageField(upload_to='imagenes_articulos', max_length=500, blank=True, verbose_name='imagen')



class Articulo(Foto):
	nombre = models.CharField(max_length=100, blank=True)
	precio = models.FloatField(blank=True)

	def __str__(self):
		return self.nombre







