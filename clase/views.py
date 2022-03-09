from django.http import HttpResponse
from django.shortcuts import render
from clase.models import Curso
import random

# Create your views here.

def nuevoCurso(request):
    curso = Curso(nombre = "A4", camada = "23789")
    curso.save()
    return HttpResponse(f"Se creo un curso: {curso.nombre}, camada {curso.camada}")
    