from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Estudiante, Profesor
from .forms import ProyectoForm, RegistroEstudianteForm, RegistroProfesorForm

def home(request):
    return render(request, 'home.html')

def proyectos_presentados(request):
    proyectos = Proyecto.objects.all()
    temas = Proyecto.TEMAS
    tema = request.GET.get('tema')
    if tema:
        proyectos = proyectos.filter(tema=tema)
    return render(request, 'proyectos_presentados.html', {'proyectos': proyectos, 'temas': temas})

def registro(request):
    if request.method == 'POST':
        form = RegistroEstudianteForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_estudiante = True
            user.save()
            estudiante = Estudiante(usuario=user, nombre=user.first_name, apellido=user.last_name, correo=user.email)
            estudiante.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistroEstudianteForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def agregar_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.estudiante = Estudiante.objects.get(usuario=request.user)
            proyecto.save()
            return redirect('proyectos_presentados')
    else:
        form = ProyectoForm()
    return render(request, 'agregar_proyecto.html', {'form': form})