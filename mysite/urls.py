from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path, include
from fotos import views
#from photos import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path(r'fotos/', include('fotos.urls')),
    #path(r'^photos/', include('mysite.photos.urls',namespace='photos')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
