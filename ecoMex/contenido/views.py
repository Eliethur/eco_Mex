from django.shortcuts import render
from django.http import HttpResponse
from registros.models import Viajes 

# Create your views here.
def inicio(request):
    return render(request, 'contenido/inicio.html')

def formulario(request):
    return render(request, 'contenido/formulario.html')

def viajesProximos(request):

    todos_los_viajes = Viajes.objects.all().order_by('fecha_salida')

    
    context = {
        'viajes_lista': todos_los_viajes
    }

    return render(request, 'contenido/viajesP.html', context)


def viajesTerminados(request):
    return render(request, 'contenido/viajesT.html')

