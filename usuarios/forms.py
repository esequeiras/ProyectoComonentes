from django import forms
#from .models import Usuario
#FloatField
class UsuarioForm(forms.Form):
    nombre=forms.CharField(required=True)
    correo=forms.CharField(required=True)
    contrasena=forms.CharField(required=True)
    fecha_nacimiiento=forms.DateTimeField()
    contrasena_confirmacion=forms.CharField(required=True)
    identificacion=forms.CharField(required=True)
    establecimiento_de_salud=forms.CharField(required=True)
    direccion=forms.CharField(required=True)
#relacion= forms.     label= algo, queryset=


 