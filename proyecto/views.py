"""
To render HTML web pages
"""
from django.http import HttpResponse
#from django.models import Usuario
from django.template.loader import render_to_string

def home_view(request):
    """
    toma un request (Django envia un request) y retorna un html
    """
    datos={
        "nombre":"eli",
        "correo":"correo@gmail.com"
    }
    
    STRING_HTML=render_to_string("home-view.html",context=datos)#el nombre del html
    return HttpResponse(STRING_HTML)