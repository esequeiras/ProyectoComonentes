from django import forms
from .models import Usuario
#from .models import Usuario
#FloatField
class UsuarioForm(forms.Form):
    nombre=forms.CharField(required=True)
    correo=forms.CharField(required=True)
    contrasena=forms.CharField(required=True)
    fecha_nacimiciento=forms.DateField()
    contrasena_confirmacion=forms.CharField(required=True)
    identificacion=forms.CharField(required=True)
    establecimiento_de_salud=forms.CharField(required=True)
    direccion=forms.CharField(required=True,widget=forms.Textarea())
    class Meta:
        widgets={
            "fecha_nacimiciento": forms.SelectDateWidget()
        }
#relacion= forms.     label= algo, queryset=
#widget


 