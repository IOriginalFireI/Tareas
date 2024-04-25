from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class tareas(models.Model):
    tarea_titulo = models.CharField(max_length=20)
    tarea_descripcion = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
