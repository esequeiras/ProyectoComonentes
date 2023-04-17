from django.contrib import admin
from django.urls import path,include
from .  import views
urlpatterns = [
    #path('',home_view),#index
    path('',views.usuario_inicio,name='inicio'),
    path('registro/',views.usuario_registro, name="registro"),
    path('modificar/<int:id>',views.usuario_modificar, name="modificar"),
    path('lista/<str:nombre>',views.doctor_view,name='lista'),
    path('medicamentos/<int:id>',views.medicamentos_view, name="medicamentos"),
    path('diagnosticos/<int:id>/<str:nombre>',views.diagnosticos_view, name="diagnosticos"),
    path('borrarDiagnostico/<int:idDiacnostico>/<int:idUs>/<str:nombre>',views.borrar_diagnosticos_view, name="borrarDiagnostico"),






]