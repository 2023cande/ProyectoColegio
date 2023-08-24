from django.shortcuts import render
from AppColegio.models import Alumno , Profesor , Entregables
from django.http import HttpResponse
from django.template import loader
from AppColegio.forms import Alumno_Form , Profesor_Form , Entregables_Form

# Create your views here.

def inicio(request):
      return render(request, "padre.html")

def alumnos(request):
      return render(request, "alumnos.html")

def profesores(request):
      return render(request, "profesores.html")

def entregables(request):
      return render(request, "entregables.html")

def alumno_formulario(request):
    if request.method == "POST":
        mi_formulario = Alumno_Form( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            alumno = Alumno( nombre=datos['nombre'] , apellido=datos['apellido'] , email=datos['email'] )
            alumno.save()
            return render( request , "alumnos.html")
    
    return render( request , "alumnos.html")


def profesor_formulario(request):
    if request.method == "POST":
        mi_formulario = Profesor_Form( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            profesor = Profesor( nombre=datos['nombre'] , apellido=datos['apellido'] , email=datos['email'] , materia=datos ['materia'] )
            profesor.save()
            return render( request , "profesores.html")
    
    return render( request , "profesores.html")

def entregables_Form(request):
    if request.method == "POST":
        mi_formulario = Entregables_Form(request.POST)

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            fechadeentrega = datos['fechadeentrega'].strftime('%Y-%m-%d')

            entregables = Entregables(nombre=datos['nombre'], apellido=datos['apellido'], fechadeentrega=fechadeentrega)
            entregables.save()
            return render(request, "entregables.html")
    
    return render(request, "entregables.html")



def buscar_alumno(request):
    return render( request , "inicio.html")


def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains = nombre)
        return render( request, "resultado_busqueda.html", {"alumnos": alumnos})
    else:
        return HttpResponse("Campo vacio")