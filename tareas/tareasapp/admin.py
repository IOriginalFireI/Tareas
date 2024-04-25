from django.contrib import admin
from .models import tareas
# Register your models here.
admin.site.register(tareas)

def __str__(self):
    return self.tarea_titulo