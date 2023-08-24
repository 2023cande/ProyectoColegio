from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    materia= models.CharField(max_length=30)

class Entregables(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    