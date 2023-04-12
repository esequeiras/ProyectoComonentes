from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.TextField()
    correo=models.TextField(primary_key=True)
    contrasena=models.TextField()
    direccion=models.TextField()
    fecha_nacimiento=models.TextField(default='')
    identificacion=models.TextField()
    establecimiento_de_salud=models.TextField()

