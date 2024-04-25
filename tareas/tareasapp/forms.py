from django import forms
from .models import tareas
from django.contrib.auth.forms import AuthenticationForm


class UserCreationForm(AuthenticationForm):
    pass

class tareas_form(forms.ModelForm):
    tarea_titulo = forms.CharField(max_length=20, label="Tarea", initial="")
    tarea_descripcion = forms.CharField(max_length=100, label="Descripción", initial="")

        

    
    class Meta:
        model = tareas
        fields = ['tarea_titulo', 'tarea_descripcion']


