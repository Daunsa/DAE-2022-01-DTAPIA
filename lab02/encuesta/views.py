from ast import Return
from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo':'formulario',
        'nombre':'daniel tapia'
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo' : 'Respuesta',
        'nombre' : request.POST['nombre'],
        'clave' : request.POST['password'],
        'educacion' : request.POST['educacion'],
        'nacionalidad' : request.POST['nacionalidad'],
        'idiomas' : request.POST.getlist['idiomas'],
        'correo' : request.POST['email'],
    }
    return render(request, 'encuesta/respuesta.html', context)