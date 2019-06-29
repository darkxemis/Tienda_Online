from django.conf.urls import url
from django.urls import path, include

from inicio import views

urlpatterns = [
	path('', views.index, name='index'),
	path('articulo/<int:articulo_id>/', views.detail, name='detail'),
]