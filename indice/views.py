
from re import template
from django.shortcuts import render
from django.template import Context, Template, loader
from django.http import HttpResponse
import random

def inicio(request):
    return render(request,'index.html', {})

def another_view(request):
    return HttpResponse('''<h1>Cuando me muera no quiero nada de flores </h1>''')

def  numero_random(request):
    numero = random.randrange(15,100)
    return HttpResponse(numero)

def  numero_(request, numero):
    texto = f'<h1>este es tu nro: {numero}</h1>'
    return HttpResponse(texto)

def mi_plantilla(request):
    
    #version vieja:
    #plantilla = open(r'C:\Users\nicol\Desktop\miproyecto\miproyecto\mi_plantilla\mi_plantilla.html')
    #template = Template(plantilla.read())
    #context = Context(diccionario_de_datos)
    #plantilla.close()
    
    nombre = 'Nicolas'
    apellido = 'Palassoli'
    lista = [1,2,3,4,5]
    
    diccionario_de_datos = {
        'nombre':nombre,
        'apellido':apellido,
        'ifNombre':len(nombre),
        'lista':lista
    }
    
    #version nueva(Loader):
    #template = loader.get_template('mi_plantilla.html')
    #plantilla_preparada = template.render(diccionario_de_datos)  
    #return HttpResponse(plantilla_preparada)

    #version Render:
    return render(request,'indice/mi_plantilla.html',diccionario_de_datos)
    