from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
    path('operaciones', views.operaciones, name='operaciones'),
    path('operaciones_respuesta', views.operaciones_respuesta, name='operaciones_respuesta'),
    path('cilindro', views.cilindro, name='cilindro'),
    path('cilindro_respuesta', views.cilindro_respuesta, name='cilindro_respuesta'),
]
