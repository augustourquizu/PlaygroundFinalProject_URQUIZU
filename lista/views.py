from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from lista.models import Lista
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class Lista(ListView):
    model = Lista
    context_object_name = 'elemento'
    template_name = "lista.html"

    
class CrearElemento(CreateView):
    model = Lista
    template_name = "crear_elemento.html"
    fields = ['descripcion', 'datos_extra', 'dia', 'imagen', 'lugar']
    success_url = reverse_lazy('lista')

class EliminarElemento(LoginRequiredMixin, DeleteView):
    model = Lista
    template_name = "eliminar_elemento.html"
    success_url = reverse_lazy('lista')

class EditarElemento(LoginRequiredMixin, UpdateView):
    model = Lista
    template_name = "editar_elemento.html"
    success_url = reverse_lazy('lista')
    fields = ['descripcion', 'datos_extra', 'dia', 'imagen', 'lugar']

class DetalleElemento(DetailView):
    model = Lista
    template_name = "detalle_elemento.html"
# Create your views here.
