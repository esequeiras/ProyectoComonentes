from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import Usuario 
from django.contrib import messages
from django.template.loader import render_to_string
from . import views
from .forms import UsuarioForm,LoginForm
# Create your views here.


def usuario_inicio(request): 
    form=LoginForm() 
    
    if request.method=="POST":
        
        # pasarle el request al formulario para que haga las validaciones del lado del servidor
        form=LoginForm(request.POST)
        if form.is_valid():
            correo=form.cleaned_data['correo']
            contrasena=form.cleaned_data['contrasena']
            
            my_lista=Usuario.objects.all()
            for us in my_lista:
                
                if us.tipo=="doctor":
                    return doctor_view(request)
                
                if us.correo==correo and us.contrasena==contrasena:
                    datos={
                        "nombre":us.nombre,
                        "correo": us.correo,
                        "identificacion":us.identificacion,
                        "establecimiento_de_salud":us.establecimiento_de_salud,
                        "direccion":us.direccion,
                        "contrasena":us.contrasena,

                    }
                    form=UsuarioForm(initial=datos)
                    #STRING_HTML=render_to_string("perfil-usuario.html",context=datos)#el nombre del html  
                    return render(request,"perfil-usuario.html",{'form':form})

            messages.add_message(request=request,level=messages.ERROR,message="Datos incorrectos, aun no tienes una cuenta?")     
        else:
            print("No valida") 
    return render(request,"inicio-usuarios.html",{'form':form})


def usuario_registro(request):
    form=UsuarioForm()

    if request.method=="POST":
        # pasarle el request al formulario para que haga las validaciones del lado del servidor
        form=UsuarioForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("informacion valida")
            usuario_nuevo=Usuario()
            usuario_nuevo.nombre=form.cleaned_data['nombre']
            usuario_nuevo.correo=form.cleaned_data['correo']
            usuario_nuevo.contrasena=form.cleaned_data['contrasena']
            usuario_nuevo.direccion=form.cleaned_data['direccion']
            usuario_nuevo.fecha_nacimiento=form['fecha_nacimiento'].value
            usuario_nuevo.identificacion=form.cleaned_data['identificacion']
            usuario_nuevo.establecimiento_de_salud=form.cleaned_data['establecimiento_de_salud']
            usuario_nuevo.save()#guardo en la bd local
           
            #Usuario.objects.create(nombre=request.POST["nombre"], correo=request.POST["correo"], contrasena=request.POST["contrasena"],direccion=request.POST["direccion"],fecha_nacimiento=request.POST["fecha_nacimiento"],identificacion=request.POST["identificacion"],establecimiento_de_salud=request.POST["establecimiento_de_salud"])
        else:
            print("No valida")
    return render(request,"registro-usuarios.html",{'form':form})


def usuario_modificar(request,datos):
    form=UsuarioForm(initial=datos)

    if request.method=="POST":
        # pasarle el request al formulario para que haga las validaciones del lado del servidor
        form=UsuarioForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("informacion valida")
            usuario_nuevo=Usuario()
            usuario_nuevo.nombre=form.cleaned_data['nombre']
            usuario_nuevo.correo=form.cleaned_data['correo']
            usuario_nuevo.contrasena=form.cleaned_data['contrasena']
            usuario_nuevo.direccion=form.cleaned_data['direccion']
            usuario_nuevo.fecha_nacimiento=form['fecha_nacimiento'].value
            usuario_nuevo.identificacion=form.cleaned_data['identificacion']
            usuario_nuevo.establecimiento_de_salud=form.cleaned_data['establecimiento_de_salud']
            usuario_nuevo.save()#guardo en la bd local
            my_lista=Usuario.objects.all()
            datos={
                "lista_objetos":my_lista 
            }
            STRING_HTML=render_to_string("home-view.html",context=datos)#el nombre del html
            return HttpResponse(STRING_HTML)           
        else:
            print("No valida")
    return render(request,"registro-usuarios.html",{'form':form})


def doctor_view(request):
    """
    toma un request (Django envia un request) y retorna un html
    """
    my_lista = Usuario.objects.filter(tipo="paciente")
    #my_lista=Usuario.objects.all()
    datos={
        "lista_objetos":my_lista 
    }
   # para crear un objesto en la bd
    # usuario=Usuario.objects.create(nombre=, correo=, contrasena)

    STRING_HTML=render_to_string("doctor-view.html",context=datos)#el nombre del html
    return HttpResponse(STRING_HTML)