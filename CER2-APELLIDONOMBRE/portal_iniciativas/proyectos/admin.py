from django.contrib import admin
from .models import Estudiante, Proyecto, Usuario, Profesor

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Proyecto)
admin.site.register(Usuario)