from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    is_profesor = models.BooleanField(default=False)
    is_estudiante = models.BooleanField(default=False)

class Estudiante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()

class Profesor(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    asignatura = models.CharField(max_length=100)

class Proyecto(models.Model):
    TEMAS = [
        ('tema 1', 'Tema 1'),
        ('tema 2', 'Tema 2'),
        ('tema 3', 'Tema 3'),
        ('tema 4', 'Tema 4'),
        ('tema 5', 'Tema 5'),
    ]

    nombre = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    tema = models.CharField(max_length=50, choices=TEMAS)
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True)
