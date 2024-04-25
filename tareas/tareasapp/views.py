from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import tareas_form, UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import tareas
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    if request.method == "GET":
        user_form = UserCreationForm()
        return render(request, "index.html", {"form_user": user_form})

    elif request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1']
            )
            user.save()
            messages.success(request, "Usuario creado")
            return redirect('index')
        else:
            return HttpResponse("Creación de usario no válida")


def login_view(request):
    if request.method == "GET":
        login_form = AuthenticationForm()
        return render(request, 'login.html', {'login_form': login_form})
    else:
        login_form = AuthenticationForm(request, request.POST)
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            errors = "Usuario o contraseña incorrectos"
            return render(request, 'login.html', {'login_form': login_form, 'errors': errors})
        else:
            login(request, user)
            return redirect('mis_tareas')


@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("index")


@login_required
def mis_tareas(request):
    form_tareas = tareas_form()
    tareas_pendientes = tareas.objects.all()
    if request.method == "GET":
        return render(request, 'mis_tareas.html', {'tareas_form': form_tareas, 'tareas': tareas_pendientes})
    else:
        form_tareas = tareas_form(request.POST)
        form_tareas_vacio = tareas_form()
        tarea_creada = "Tarea guardada."
        if form_tareas.is_valid():
            tarea = form_tareas.save(commit=False)
            tarea.user = request.user
            tarea.save()
            return render(request, 'mis_tareas.html', {'tareas_form': form_tareas_vacio, 'tareas': tareas_pendientes, 'tarea_guardada': tarea_creada})


@login_required
def eliminar_tarea(request):
    if request.method == "POST":
        tarea_id = request.POST.get('tarea_id')
        tarea = get_object_or_404(tareas, id=tarea_id)
        tarea.delete()
        return redirect('mis_tareas')


@login_required
def detalle_tarea(request, tarea_id):

    if request.method == "GET":
        tarea = get_object_or_404(tareas, pk=tarea_id, user=request.user)
        form = tareas_form(instance=tarea)
        return render(request, "detalle_tarea.html", {"tarea": tarea, "form": form})

    else:

        try:
            tarea = get_object_or_404(tareas, pk=tarea_id, user=request.user)
            form = tareas_form(request.POST, instance=tarea)
            form.save()
            return redirect("mis_tareas")
        except ValueError:
            return render(request, "detalle_tarea.html", {"tarea": tarea, "form": form, 'error': "Error al actualizar tarea"})
