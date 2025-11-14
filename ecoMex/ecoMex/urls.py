from django.contrib import admin
from django.urls import path
from contenido import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('formulario/', views.formulario, name='formulario_preinscripcion'),
    path('viajesP/', views.viajesProximos, name='viajes_proximos'),
    path('viajesT/', views.viajesTerminados, name='viajes_terminados'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)