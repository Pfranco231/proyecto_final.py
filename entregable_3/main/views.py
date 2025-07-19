from django.shortcuts import render, redirect
from .models import *
from .forms import *

def inicio(request):
    return render(request, "main/inicio.html")

def agregar_consolas(request):
    if request.method == 'POST':
        form = consolasForm(request.POST)
        if form.is_valid():
            consola_de_juegos = consolas(
                #cleaned_data es lo que se guarda en el formulario
                modelo=form.cleaned_data['modelo'],
                empresa=form.cleaned_data['empresa'],
                precio=form.cleaned_data['precio'],
                fecha_de_creacion=form.cleaned_data['fecha_de_creacion'],
            )
            consola_de_juegos.save()
            return render(request, "main/correcto.html")
        
    elif request.method == 'GET':
        form = consolasForm()                                #aca mandamo el formulario vacio
        return render(request, "main/agregar_consolas.html", {"form": form})
    

def agregar_juegos(request):
    if request.method == 'POST':
        form = juegosForm(request.POST)
        if form.is_valid():
            videojuegos = juegos(
                juego=form.cleaned_data['juego'],
                empresa=form.cleaned_data['empresa'],
                categoria=form.cleaned_data['categoria'],
                precio=form.cleaned_data['precio'],
            )
            videojuegos.save()
            return render(request, "main/correcto.html")
    elif request.method == 'GET':
        form = juegosForm()
        return render(request, "main/agregar_juegos.html", {"form": form})

def agregar_accesorios(request):
    if request.method == 'POST':
        form = accesoriosForm(request.POST)
        if form.is_valid():
            accesorios_para_consolas = accesorios(
                producto=form.cleaned_data['producto'],
                empresa=form.cleaned_data['empresa'],
                duracion_bateria=form.cleaned_data['duracion_bateria'],
                precio=form.cleaned_data['precio'],
            )
            accesorios_para_consolas.save()
            return render(request, "main/correcto.html")
    elif request.method == 'GET':
        form = accesoriosForm()
        return render(request, "main/agregar_accesorios.html", {"form": form})