from django.contrib import admin

# Register your models here.
from .models import *
from jet.admin import CompactInline 
from image_cropping import ImageCroppingMixin

class ArticuloFotoInline(ImageCroppingMixin, CompactInline): 	
	model = ArticuloImagen 	
	extra = 0

class AdminArtitulo(admin.ModelAdmin, ImageCroppingMixin):
	list_display = ['nombre', 'precio']
	inlines = [ArticuloFotoInline, ]
	fieldsets = (
		(u'contenido', {
			'fields': ("nombre", "precio")
			}),
		)

	def precio_euros(self, obj):
		return str(obj.precio) + ' €'

'''class AdminFoto(admin.ModelAdmin):
	list_display = ['nombre_foto', 'foto', 'reporter']
	fieldsets = (
		(u'contenido', {
			'fields': ('nombre_foto', 'foto', 'reporter')
			}),
		)'''

		#list_filter = ["nombre"]
		#list_editable = ["nombre"]
		#search_fields = ["nombre"]

	

admin.site.register(Articulo, AdminArtitulo)
#admin.site.register(Foto, AdminFoto)



