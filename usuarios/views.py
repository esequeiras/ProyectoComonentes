from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from usuarios.models import Usuario 
from django.template.loader import render_to_string
from . import views

def usuario_inicio(request):   
   # STRING_HTML=render_to_string("<h1>Inicio usuario</h1>")#el nombre del html
    return HttpResponse('<h1>Inicio usuario</h1>')

def usuario_registro(request):   
    #STRING_HTML=render_to_string("<h1>registro usuario</h1>")#el nombre del html
    return HttpResponse('<h1>registro usuario</h1>')