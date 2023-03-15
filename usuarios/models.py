from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre=models.TextField()
    correo=models.TextField()
