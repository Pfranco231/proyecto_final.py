from django.shortcuts import render, redirect

def inicio(request):
    return render(request, "main/inicio.html")
