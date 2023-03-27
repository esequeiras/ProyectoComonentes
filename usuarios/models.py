from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.TextField()
    correo=models.TextField()
    contrasena=models.TextField()
    dierccion=models.TextField()
    fecha_nacimiiento=models.DateField()
    identificacion=models.TextField()
    establecimiento_de_salud=models.TextField()

