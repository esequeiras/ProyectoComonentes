from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from usuarios.models import Usuario 
from django.template.loader import render_to_string
from . import views
from .forms import UsuarioForm,LoginForm

def usuario_inicio(request): 
    form=LoginForm() 
    
    if request.method=="POST":
        # pasarle el request al formulario para que haga las validaciones del lado del servidor
        form=LoginForm(request.POST)
        if form.is_valid():
            print("informacion valida")
   
            correo=form.cleaned_data['correo']
            contrasena=form.cleaned_data['contrasena']
            my_lista=Usuario.objects.all()
            for us in my_lista:
                if us.correo==correo and us.contrasena==contrasena:
                    datos={
                        "nombre":us.nombre
                    }
                    STRING_HTML=render_to_string("perfil-usuario.html",context=datos)#el nombre del html
                    return HttpResponse(STRING_HTML)
                else:
                    print('El usuario no se encontro')                
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
            #usuario_nuevo.fecha_nacimiento=form.cleaned_data['fecha_nacimiento']
            usuario_nuevo.identificacion=form.cleaned_data['identificacion']
            usuario_nuevo.establecimiento_de_salud=form.cleaned_data['establecimiento_de_salud']
            usuario_nuevo.save()#guardo en la bd local
            my_lista=Usuario.objects.all()
            datos={
                "lista_objetos":my_lista 
            }
            STRING_HTML=render_to_string("home-view.html",context=datos)#el nombre del html
            return HttpResponse(STRING_HTML)
           
           
            #Usuario.objects.create(nombre=request.POST["nombre"], correo=request.POST["correo"], contrasena=request.POST["contrasena"],direccion=request.POST["direccion"],fecha_nacimiento=request.POST["fecha_nacimiento"],identificacion=request.POST["identificacion"],establecimiento_de_salud=request.POST["establecimiento_de_salud"])
        else:
            print("No valida")

   # para crear un objesto en la bd
    # usuario=Usuario.objects.create(nombre=, correo=, contrasena)
        
    
    
    #STRING_HTML=render_to_string("registro-usuarios.html",{'form':form})
    #STRING_HTML=render_to_string("home-view.html")#el nombre del html
    #return render(request,'home-view.html',context=datos)
    return render(request,"registro-usuarios.html",{'form':form})


def home_view(request):
    """
    toma un request (Django envia un request) y retorna un html
    """
    my_lista=Usuario.objects.all()
    datos={
        "lista_objetos":my_lista 
    }
   # para crear un objesto en la bd
    # usuario=Usuario.objects.create(nombre=, correo=, contrasena)
    
    STRING_HTML=render_to_string("home-view.html",context=datos)#el nombre del html
    return HttpResponse(STRING_HTML)