from django.shortcuts import render, redirect
from .models import *
from .forms import *

def inicio(request):
    return render(request, "main/inicio.html")

def agregar_consolas(request):
    if request.method == 'POST':
        form = consolasForm(request.POST)
        if form.is_valid():
            consolas = consolas(
                #cleaned_data es lo que se guarda en el formulario
                modelo=form.cleaned_data['modelo'],
                empresa=form.cleaned_data['empresa'],
                precio=form.cleaned_data['precio'],
                fecha_de_creacion=form.cleaned_data['fecha_de_creacion'],
            )
            consolas.save()
            return redirect('inicio')
        
    elif request.method == 'GET':
        form = consolasForm()                                #aca mandamo el formulario vacio
        return render(request, "main/agregar_consolas.html", {"form": form})
    

def agregar_juegos(request):
    if request.method == 'POST':
        form = juegosForm(request.POST)
        if form.is_valid():
            juegos = juegos(
                juego=form.cleaned_data['juego'],
                empresa=form.cleaned_data['empresa'],
                categoria=form.cleaned_data['cateria'],
                precio=form.cleaned_data['precio'],
            )
            juegos.save()
            return redirect('inicio')
    elif request.method == 'GET':
        form = juegosForm()
        return render(request, "main/agregar_juegos.html", {"form": form})

def agregar_accesorios(request):
    if request.method == 'POST':
        form = accesoriosForm(request.POST)
        if form.is_valid():
            accesorios = accesorios(
                producto=form.cleaned_data['producto'],
                empresa=form.cleaned_data['empresa'],
                duracion_bateria=form.cleaned_data['duracion_bateria'],
                precio=form.cleaned_data['precio'],
            )
            accesorios.save()
            return redirect('inicio')
    elif request.method == 'GET':
        form = accesoriosForm()
        return render(request, "main/agregar_accesorios.html", {"form": form})