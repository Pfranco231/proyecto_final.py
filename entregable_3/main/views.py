from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class InicioView(ListView):
    model = consolas
    template_name = 'main/inicio.html'
    context_object_name = 'consolas'
    
    def get_queryset(self):
        modelo = self.request.GET.get('modelo', '')
        if modelo:
            return consolas.objects.filter(modelo__icontains=modelo)
        return consolas.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modelo'] = self.request.GET.get('modelo', '')
        return context
    
    

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


class AboutView(TemplateView):
    template_name = "main/about.html"



class ConsolaDetailView(DetailView):
    model = consolas
    template_name = 'main/consola_detalle.html'
    context_object_name = 'consola'
    
#@login_required
class ConsolaCreateView(LoginRequiredMixin, CreateView):
    model = consolas
    template_name = 'main/consola_form.html'
    fields = ['imagen', 'modelo', 'empresa', 'precio', 'fecha_de_creacion']
    success_url = reverse_lazy('inicio')

#@login_required
class ConsolaUpdateView(LoginRequiredMixin, UpdateView):
    model = consolas
    template_name = 'main/consola_form.html'
    fields = ['imagen', 'modelo', 'empresa', 'precio', 'fecha_de_creacion',]
    success_url = reverse_lazy('inicio')
    


#@login_required
class ConsolaDeleteView(LoginRequiredMixin, DeleteView):
    model = consolas
    template_name = 'main/consola_confirm_delete.html'
    success_url = reverse_lazy('inicio')
    

