from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
def inicio(request):
    return render(request, "base.html")

def registrar(request):
    formulario=UserCreationForm(request.POST)
    if formulario.is_valid():
        formulario.save()
        return redirect("inicio")
    return render(request, "usuarios/registrar.html", {"formulario":formulario})
# Create your views here.
