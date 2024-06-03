from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Proyecto, Profesor

class RegistroEstudianteForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class RegistroProfesorForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields =['username', 'asignatura','password1', 'password2']

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'tema', 'profesor']
