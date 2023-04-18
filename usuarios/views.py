from datetime import date
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import Usuario,Medicina,Diagnostico
from django.contrib import messages
from django.template.loader import render_to_string
from . import views
from .forms import UsuarioForm,LoginForm,MedicamentoForm,DiagnosticoForm
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
                    global LOG_US
                    LOG_US = us
                    if us.tipo=="doctor":
                        return doctor_view(request)
                    medicinas=Medicina.objects.filter(paciente_id=us.pk) #Filtro por llave foránea
                    diagnosticos=Diagnostico.objects.filter(pacienteD_id=us.pk) #Filtro por llave foránea
                    

                    datos={
                        "id":us.pk,
                        "nombre":us.nombre,
                        "correo": us.correo,
                        "lista_medicinas": medicinas,
                        "lista_diagnosticos":diagnosticos
                    } 
                    
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
        if request.POST['contrasena']!=request.POST['contrasena_confirmacion']:
            messages.add_message(request=request,level=messages.ERROR,message="Las contraseñas no coinciden")     
        else:
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
    return render(request,"registro-usuarios.html",{'form':UsuarioForm()})


def usuario_modificar(request):
    global LOG_US
    
    if request.method=="POST":
        usuario_nuevo=Usuario()
        usuario_nuevo.pk=LOG_US.pk
        usuario_nuevo.nombre=request.POST['nombre']
        usuario_nuevo.correo=LOG_US.correo
        usuario_nuevo.contrasena=request.POST['contrasena']
        usuario_nuevo.direccion=request.POST['direccion']
        usuario_nuevo.fecha_nacimiento=request.POST['fecha_nacimiento']
        usuario_nuevo.identificacion=LOG_US.identificacion
        usuario_nuevo.establecimiento_de_salud=request.POST['establecimiento_de_salud']
        usuario_nuevo.save()#guardo en la bd local
        return render(request,"modificar-usuario.html",{'us':Usuario.objects.get(id=usuario_nuevo.pk)})
    return render(request,"modificar-usuario.html",{'us':Usuario.objects.get(id=LOG_US.pk)})
def perfil_usuario(request):
    global LOG_US
    medicinas=Medicina.objects.filter(paciente_id=LOG_US.pk) #Filtro por llave foránea
    diagnosticos=Diagnostico.objects.filter(pacienteD_id=LOG_US.pk) #Filtro por llave foránea
    datos={
        "id":LOG_US.pk,
        "nombre":LOG_US.nombre,
        "correo": LOG_US.correo,
        "lista_medicinas": medicinas,
        "lista_diagnosticos":diagnosticos
    } 
    return render(request,"perfil-usuario.html",datos)
#listar pacientes
def doctor_view(request):
    """
    toma un request (Django envia un request) y retorna un html
    """
    my_lista = Usuario.objects.filter(tipo="paciente")
    #my_lista=Usuario.objects.all()
    print(my_lista)
    datos={
        "lista_objetos":my_lista,
        "us":LOG_US.nombre
    }
   # para crear un objesto en la bd
    # usuario=Usuario.objects.create(nombre=, correo=, contrasena)

    STRING_HTML=render_to_string("doctor-view.html",context=datos)#el nombre del html
    return HttpResponse(STRING_HTML)
#Registra medicamentos del usuario

#L------------------------------------------------------------medicamentos del usuario----------------------------------------------------------------------
def medicamentos_view(request,idUs):

    medicinas=Medicina.objects.filter(paciente_id=idUs) #Filtro por llave foránea
    datos={
        "lista_medicinas": medicinas,
        "idPaciente":idUs
    } 

    STRING_HTML=render_to_string(request=request,template_name="lista-medicamentos.html",context=datos)#el nombre del html
    return HttpResponse(STRING_HTML)

def registro_medicamentos_view(request,idUs):
    if request.method=="POST":
    # pasarle el request al formulario para que haga las validaciones del lado del servidor
        form=MedicamentoForm(request.POST)
        print(request.POST)
        print(form.errors)

        if form.is_valid():
            print("informacion valida")
            medicina_nueva=Medicina()
            medicina_nueva.medicamento=form.cleaned_data['medicamento']
            medicina_nueva.fecha_prescripcion=datetime.now().date()
            medicina_nueva.indicacion=form.cleaned_data['indicacion']
            medicina_nueva.mese_tratamiento=form.cleaned_data['mese_tratamiento']
            medicina_nueva.paciente=Usuario.objects.get(id=idUs)
            medicina_nueva.save()#guardo en la bd local    
        else:
            print("No valida")
    STRING_HTML=render_to_string(request=request,template_name="registrar-medicamentos.html", context={"form":MedicamentoForm(),"idPaciente":idUs})#el nombre del html
    return HttpResponse(STRING_HTML)

def borrar_medicina_view(request,idMed,idUs):
    medicinaBorrar=Medicina.objects.get(id=idMed)
    medicinaBorrar.delete()
    medicinas=Medicina.objects.filter(paciente_id=idUs) #Filtro por llave foránea
    
    datos={
        "lista_medicinas": medicinas,
        "idPaciente":idUs
    } 
    STRING_HTML=render_to_string(template_name="lista-medicamentos.html",context=datos)#el nombre del html
    return HttpResponse(STRING_HTML)
#L------------------------------------------------------------diagnosticos del usuario----------------------------------------------------------------------

def diagnosticos_view(request,idUs):
    diagnosticos=Diagnostico.objects.filter(pacienteD_id=idUs) #Filtro por llave foránea
    datos={
        "lista_diagnosticos":diagnosticos,
        "idPaciente":idUs
    } 

    if request.method=="POST":
        # pasarle el request al formulario para que haga las validaciones del lado del servidor
        form=DiagnosticoForm(request.POST)

        if form.is_valid():
            print("informacion valida")
            diagnostico_nuevo=Diagnostico()
            diagnostico_nuevo.diagnostico=form.cleaned_data['diagnostico']
            diagnostico_nuevo.fecha=datetime.now().date()
            diagnostico_nuevo.estado=form.cleaned_data['estado']
            diagnostico_nuevo.doctor=LOG_US.nombre
            diagnostico_nuevo.pacienteD=Usuario.objects.get(id=id)
            diagnostico_nuevo.save()#guardo en la bd local
        else:
            print("No valida")
    STRING_HTML=render_to_string(request=request,template_name="lista-diagnosticos.html",context=datos)#el nombre del html
    return HttpResponse(STRING_HTML)

def registro_diagnosticos_view(request,idUs):

    if request.method=="POST":
        # pasarle el request al formulario para que haga las validaciones del lado del servidor
        form=DiagnosticoForm(request.POST)

        if form.is_valid():
            print("informacion valida")
            diagnostico_nuevo=Diagnostico()
            diagnostico_nuevo.diagnostico=form.cleaned_data['diagnostico']
            diagnostico_nuevo.fecha=datetime.now().date()
            diagnostico_nuevo.estado=form.cleaned_data['estado']
            diagnostico_nuevo.doctor=LOG_US.nombre
            diagnostico_nuevo.pacienteD=Usuario.objects.get(id=idUs)
            diagnostico_nuevo.save()#guardo en la bd local
        else:
            print("No valida")
    STRING_HTML=render_to_string(request=request,template_name="registro-disagnostico.html", context={"form":DiagnosticoForm(),"idPaciente":idUs})#el nombre del html
    return HttpResponse(STRING_HTML)

def borrar_diagnosticos_view(request,idDiacnostico,idUs):
    diagnosticoBorrar=Diagnostico.objects.get(id=idDiacnostico)
    diagnosticoBorrar.delete()
    diagnosticos=Diagnostico.objects.filter(pacienteD_id=idUs) #Filtro por llave foránea
    
    datos={
        "lista_diagnosticos":diagnosticos,
        "idPaciente":idUs
        
    } 

    STRING_HTML=render_to_string(template_name="lista-diagnosticos.html",context=datos)#el nombre del html
    return HttpResponse(STRING_HTML)
