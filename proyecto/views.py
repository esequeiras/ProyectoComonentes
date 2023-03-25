"""
To render HTML web pages
"""
from django.http import HttpResponse
from usuarios.models import Usuario 
from django.template.loader import render_to_string



def home_view(request):
    """
    toma un request (Django envia un request) y retorna un html
    """
    us=Usuario.objects.get(id=1)

    datos={
        "nombre":us.nombre,
        "correo":us.correo,
        "contrasena":us.contrasena
    }
   # para crear un objesto en la bd
    # usuario=Usuario.objects.create(nombre=, correo=, contrasena)
    print("este es el correo del usuario",us.correo)
    
    STRING_HTML=render_to_string("home-view.html",context=datos)#el nombre del html
    return HttpResponse(STRING_HTML)