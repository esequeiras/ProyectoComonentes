from django import forms
from .models import Usuario
#from .models import Usuario
#FloatField

class DateInput(forms.DateInput):
    input_type='date'
class NumberInput(forms.NumberInput):
    input_type='number'
class UsuarioForm(forms.Form):
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Nombre",required=True)
    correo=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Correo Electrónico",required=True)
    contrasena=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Contraseña',required=True)
    fecha_nacimiento=forms.CharField(required=False,widget=DateInput(attrs={'class':'form-control'}))

    contrasena_confirmacion=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Confirmar contraseña',required=True)
    identificacion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Identificación',required=True)
    establecimiento_de_salud=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Establecimiento de salud',required=True)
    direccion=forms.CharField(required=True,widget=forms.Textarea(attrs={ 'rows':3, 'cols':30,'class':'form-control'}))

#relacion= forms.     label= algo, queryset=
#widget
class LoginForm(forms.Form):
    correo=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm'}),label='Correo Electrónico',required=True)
    contrasena=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm'}),label='Contraseña',required=True)

class MedicamentoForm(forms.Form):
    medicamento=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Medicamento",required=True)
    indicacion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Indicacion",required=True)
    mese_tratamiento=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}),label="Meses Tratamiento",required=True)
    
class DiagnosticoForm(forms.Form):
    diagnostico=forms.CharField(widget=forms.Textarea(attrs={ 'rows':3, 'cols':30,'class':'form-control'}),label="Diagnostico",required=True)
    estado=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Estado",required=True)
    
    
 