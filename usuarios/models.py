from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.TextField()
    correo=models.TextField()
    contrasena=models.TextField()
    direccion=models.TextField()
    fecha_nacimiento=models.TextField(default='')
    identificacion=models.TextField()
    establecimiento_de_salud=models.TextField()
    tipo=models.TextField(default='paciente')

class Medicina(models.Model):
    medicamento=models.TextField()
    fecha_prescripcion=models.TextField()
    indicacion=models.TextField()
    mese_tratamiento=models.TextField()
    paciente=models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Diagnostico(models.Model):
    diagnostico=models.TextField()
    fecha=models.TextField()
    estado=models.TextField()
    doctor=models.TextField()
    pacienteD=models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)

