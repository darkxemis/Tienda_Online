from django.db import models

from django.conf import settings

#Import para las imagenes en galleria, si queremos asociar un articulo con más de una imagen
from image_cropping import ImageRatioField 
from easy_thumbnails.files import get_thumbnailer

#Import para el campo de moneda
from djmoney.models.fields import MoneyField
from django.db import models

#Import para texto con formato APP
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Articulo(models.Model):
	nombre = models.CharField(max_length=100, blank=True)
	precio = MoneyField(max_digits=14, decimal_places=2, default_currency='EUR')
	text = RichTextUploadingField(verbose_name='Texto', null=True, blank=True) 

	def __str__(self):
		return self.nombre

class Foto(models.Model):
	nombre_foto = models.CharField(max_length=100, blank=True)
	foto = models.ImageField(upload_to='imagenes_articulos', max_length=500, blank=True, verbose_name='imagen')
	#reporter = models.ForeignKey(Articulo, on_delete=models.CASCADE)
	
	class Meta:         
		abstract = True         
		verbose_name = 'Imagen'         
		verbose_name_plural = u'Galería'

	def __str__(self):         
		return u'Imagen: ' + str(self.id)

	def __str__(self):
	    return self.nombre_foto

	#class Meta:
	 #   ordering = ('nombre_foto',)

class ArticuloImagen(Foto):
		cropping = ImageRatioField('foto', '300x300', verbose_name=u'Recorte visible') 	
		articulo = models.ForeignKey(Articulo, related_name='imagenes_articulos', null=True, on_delete=models.CASCADE)  	
		def get_img(self): 		
			return get_thumbnailer(self.image).get_thumbnail({'size': (300, 300), 'box': self.cropping, 'crop': True, 'detail': True }).url 








