from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from usuarios.models import Usuario 
from django.template.loader import render_to_string
from . import views
from .forms import UsuarioForm

def usuario_inicio(request):   
    STRING_HTML=render_to_string("inicio-usuarios.html")#el nombre del html
    
    return HttpResponse(STRING_HTML)

def usuario_registro(request):
    form=UsuarioForm()

    if request.method=="POST":
        # pasarle el request al formulario para que haga las validaciones del lado del servidor
        form=UsuarioForm(request.POST)
        if form.is_valid():
            print("informacion valida")
            usuario_nuevo=Usuario()
            usuario_nuevo.nombre=form.cleaned_data['nombre']
            usuario_nuevo.correo=form.cleaned_data['correo']
            usuario_nuevo.contrasena=form.cleaned_data['contrasena']
            usuario_nuevo.direccion=form.cleaned_data['direccion']
            usuario_nuevo.fecha_nacimiento=form.cleaned_data['fecha_nacimiento']
            usuario_nuevo.identificacion=form.cleaned_data['identificacion']
            usuario_nuevo.establecimiento_de_salud=form.cleaned_data['establecimiento_de_salud']
            usuario_nuevo.save()#guardo en la bd local

            #Usuario.objects.create(nombre=request.POST["nombre"], correo=request.POST["correo"], contrasena=request.POST["contrasena"],direccion=request.POST["direccion"],fecha_nacimiento=request.POST["fecha_nacimiento"],identificacion=request.POST["identificacion"],establecimiento_de_salud=request.POST["establecimiento_de_salud"])
        else:
            print("No valida")

   # para crear un objesto en la bd
    # usuario=Usuario.objects.create(nombre=, correo=, contrasena)
        
    
    
    #STRING_HTML=render_to_string("registro-usuarios.html",{'form':form})
    #STRING_HTML=render_to_string("home-view.html")#el nombre del html
    #return render(request,'home-view.html',context=datos)
    return render(request,"registro-usuarios.html",{'form':form})
