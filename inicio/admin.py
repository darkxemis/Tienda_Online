from django.contrib import admin

# Register your models here.
from .models import *

class AdminArtitulo(admin.ModelAdmin):
	list_display = ["nombre", 'precio_euros', "foto", "nombre_foto"]
	fieldsets = (
		(u'contenido', {
			'fields': ("nombre", "precio", "foto", "nombre_foto")
			}),
		)

	def precio_euros(self, obj):
		return str(obj.precio) + ' €'

		#list_filter = ["nombre"]
		#list_editable = ["nombre"]
		#search_fields = ["nombre"]

	

admin.site.register(Articulo, AdminArtitulo)
