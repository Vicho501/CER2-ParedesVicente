from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('proyectos/', views.proyectos_presentados, name='proyectos_presentados'),
    path('registro/', views.registro, name='registro'),
    path('agregar_proyecto/', views.agregar_proyecto, name='agregar_proyecto'),
    
]