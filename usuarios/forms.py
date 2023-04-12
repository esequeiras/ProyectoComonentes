from django import forms
from .models import Usuario
#from .models import Usuario
#FloatField

class DateInput(forms.DateInput):
    input_type='date'
    
class UsuarioForm(forms.Form):
    nombre=forms.CharField(label="Nombre",required=True)
    correo=forms.CharField(label="Correo Electrónico",required=True)
    contrasena=forms.CharField(widget=forms.PasswordInput,label='Contraseña',required=True)
    fecha_nacimiento=forms.CharField(required=False,widget=DateInput)

    contrasena_confirmacion=forms.CharField(widget=forms.PasswordInput,label='Confirmar contraseña',required=True)
    identificacion=forms.CharField(label='Identificación',required=True)
    establecimiento_de_salud=forms.CharField(label='Establecimiento de salud',required=True)
    direccion=forms.CharField(required=True,widget=forms.Textarea(attrs={ 'rows':3, 'cols':30}))

#relacion= forms.     label= algo, queryset=
#widget
class LoginForm(forms.Form):
    correo=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}),label='Correo Electrónico',required=True)
    contrasena=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}),label='Contraseña',required=True)

 