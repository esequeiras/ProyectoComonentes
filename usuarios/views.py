from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import Usuario,Medicina
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
                
                
                
                if us.correo==correo and us.contrasena==contrasena:
                    if us.tipo=="doctor":
                        return doctor_view(request)
                    medicinas=Medicina.objects.filter(paciente_id=us.pk) #Filtro por llave foránea
                    diagnosticos=Medicina.objects.filter(paciente_id=us.pk) #Filtro por llave foránea

                    datos={
                        "id":us.pk,
                        "nombre":us.nombre,
                        "correo": us.correo,
                        "lista_medicinas": medicinas,
                        "lista_diagnosticos":diagnosticos
                    } 
                    print(medicinas)
                    form=UsuarioForm(initial=datos)
                    #STRING_HTML=render_to_string("perfil-usuario.html",context=datos)#el nombre del html  
                    return render(request,"perfil-usuario.html",datos)

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
            usuario_nuevo.fecha_nacimiento=form['fecha_nacimiento'].value()
            usuario_nuevo.identificacion=form.cleaned_data['identificacion']
            usuario_nuevo.establecimiento_de_salud=form.cleaned_data['establecimiento_de_salud']
            usuario_nuevo.save()#guardo en la bd local
           
            #Usuario.objects.create(nombre=request.POST["nombre"], correo=request.POST["correo"], contrasena=request.POST["contrasena"],direccion=request.POST["direccion"],fecha_nacimiento=request.POST["fecha_nacimiento"],identificacion=request.POST["identificacion"],establecimiento_de_salud=request.POST["establecimiento_de_salud"])
        else:
            print("No valida")
    return render(request,"registro-usuarios.html",{'form':form})


def usuario_modificar(request,id):
    usuario_log=Usuario.objects.get(id=id)
    print(usuario_log.contrasena)

    datos={
        "nombre":usuario_log.nombre,
        "correo": usuario_log.correo,
        "contrasena":usuario_log.contrasena,
        "fecha_nacimiento":usuario_log.fecha_nacimiento,
        "establecimiento_de_salud":usuario_log.establecimiento_de_salud,
        "identificacion":usuario_log.identificacion,
        "direccion":usuario_log.direccion
    }
    form=UsuarioForm(initial=datos)
    #form["correo"].field.widget.attrs['disabled'] = True
    #form["identificacion"].field.widget.attrs['disabled'] = True

    if request.method=="POST":
        # pasarle el request al formulario para que haga las validaciones del lado del servidor
        form=UsuarioForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print("informacion valida")
            usuario_nuevo=Usuario()
            usuario_nuevo.pk=usuario_log.pk
            usuario_nuevo.nombre=form.cleaned_data['nombre']
            usuario_nuevo.correo=usuario_log.correo
            usuario_nuevo.contrasena=form.cleaned_data['contrasena']
            usuario_nuevo.direccion=form.cleaned_data['direccion']
            usuario_nuevo.fecha_nacimiento=form['fecha_nacimiento'].value()
            usuario_nuevo.identificacion=usuario_log.identificacion
            usuario_nuevo.establecimiento_de_salud=form.cleaned_data['establecimiento_de_salud']
            usuario_nuevo.save()#guardo en la bd local
            return render(request,"modificar-usuario.html",{'form':form})
        else:
            print("No valida")
    return render(request,"modificar-usuario.html",{'form':form})


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