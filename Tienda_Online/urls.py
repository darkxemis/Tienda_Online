"""Tienda_Online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import url

from django.conf.urls.static import serve, static

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('', include('inicio.urls')),
    re_path('ckeditor/', include('ckeditor_uploader.urls')), #URL para el texto con formato
    #url(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT, }), 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
