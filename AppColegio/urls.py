from django.urls import path
from . import views

urlpatterns = [
    path("" , views.inicio , name="inicio"),
    path("profesores" , views.profesores , name="profesores"),
    path("alumnos" , views.alumnos , name="alumnos"),
    path("entregables", views.entregables, name="entregables"),
    path("alta_alumno", views.alumno_formulario , name="alta_alumno"),
    path("alta_profesor" , views.profesor_formulario , name="alta_profesor"), 
    path("buscar_alumno" , views.buscar_alumno , name="buscar_alumno"),
    path("buscar", views.buscar)

]
