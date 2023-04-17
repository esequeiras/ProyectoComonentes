from django.contrib import admin
from django.urls import path,include
from .  import views
urlpatterns = [
    #path('',home_view),#index
    path('',views.usuario_inicio,name='inicio'),
    path('registro/',views.usuario_registro, name="registro"),
    path('modificar/<int:id>',views.usuario_modificar, name="modificar"),
    path('lista/',views.doctor_view,name='lista'),

    #Registro listado y borrado de medicamentos
    path('medicamentos/<int:idUs>',views.medicamentos_view, name="medicamentos"),
    path('borrarMedicina/<int:idMed>/<int:idUs>',views.borrar_medicina_view, name="borrarMedicina"),
    path('registrarMed/<int:idUs>',views.registro_medicamentos_view, name="registrarMed"),


    path('diagnosticos/<int:id>',views.diagnosticos_view, name="diagnosticos"),
    path('borrarDiagnostico/<int:idDiacnostico>/<int:idUs>/<str:nombre>',views.borrar_diagnosticos_view, name="borrarDiagnostico"),







]