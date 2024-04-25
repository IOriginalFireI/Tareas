"""
URL configuration for tareas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tareasapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('ingresar/', views.login_view, name="ingresar"),
    path('ingresar/mistareas/salir/', views.logout_view, name="salir"),
    path('ingresar/mistareas/', views.mis_tareas, name="mis_tareas"),
    path('ingresar/mistareas/eliminar', views.eliminar_tarea, name="eliminar_tarea"),
    path('ingresar/mistareas/<int:tarea_id>', views.detalle_tarea, name="detalle_tarea")
]
