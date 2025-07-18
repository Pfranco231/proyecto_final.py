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
        form = consolasForm()                                          #aca mandamo el formulario vacio
        return render(request, "main/agregar_consolas.html", {"form": form})
    

    def agregar_juegos(request):
        if request.method == 'POST':
            #no se por me da advertencia
            form = juegosForm(request.POST)
            if form.is_valid():
                juegos = juegos(
                    #resivar esto
                    nombre=form.cleaned_data['nombre'],
                    genero=form.cleaned_data['genero'],
                    precio=form.cleaned_data['precio'],
                    fecha_de_lanzamiento=form.cleaned_data['fecha_de_lanzamiento'],
                )
                juegos.save()
                return redirect('inicio')
        elif request.method == 'GET':
            #y aqui tambien
            form = juegosForm()
            return render(request, "main/agregar_juegos.html", {"form": form})

    def agregar_accesorios(request):
        if request.method == 'POST':
            form = accesoriosForm(request.POST)
            if form.is_valid():
                accesorios = accesorios(
                    #revisar esto
                    nombre=form.cleaned_data['nombre'],
                    tipo=form.cleaned_data['tipo'],
                    precio=form.cleaned_data['precio'],
                    compatibilidad=form.cleaned_data['compatibilidad'],
                )
                accesorios.save()
                return redirect('inicio')
        elif request.method == 'GET':
            form = accesoriosForm()
            return render(request, "main/agregar_accesorios.html", {"form": form})