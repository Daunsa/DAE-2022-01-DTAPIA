from ast import Return
from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render
import parser
import math

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
        'idiomas' : request.POST.getlist('idiomas'),
        'correo' : request.POST['email'],
        'website' : request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)

def operaciones_respuesta(request):
    exprecion = parser.expr(request.POST['num_1'] + request.POST['operaciones'] + request.POST['num_2']).compile()
    resultado = eval(exprecion)
    context = {
        'titulo' : 'Respuesta',
        'resultado' : resultado,
    }
    return render(request, 'encuesta/operaciones_respuesta.html', context)

def operaciones(request):
    return render(request, 'encuesta/operaciones.html')

def cilindro_respuesta(request):
    exprecion = parser.expr("((" + request.POST['num_2'] + "/2)**2)*" + request.POST['num_1']).compile()
    resultado = float(eval(exprecion)) * math.radians(180)
    
    context = {
        'titulo' : 'Respuesta',
        'resultado' : resultado,
    }
    return render(request, 'encuesta/cilindro_respuesta.html', context)

def cilindro(request):
    return render(request, 'encuesta/cilindro.html')