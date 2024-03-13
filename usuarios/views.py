from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import CreacionDeUsuario, EditarPerfil
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtras


class EditarContrasenia(PasswordChangeView):
    template_name = 'cambiar_contrasenia.html'
    success_url = reverse_lazy('perfil')
    

def inicio(request):
    return render(request, "base.html", locals())

def login(request):
    formulario=AuthenticationForm()
    if request.method=="POST":
        formulario=AuthenticationForm(request, data=request.POST)
    if formulario.is_valid():
        usuario=formulario.cleaned_data.get("username")
        contrasenia=formulario.cleaned_data.get("password")
        user=authenticate(username=usuario, password=contrasenia)
        django_login(request, user)
        return redirect("inicio")
    return render(request, "login.html", {"formulario":formulario})
# Create your views here.

def registrar(request):
    formulario=CreacionDeUsuario()
    if request.method=="POST":
        formulario=CreacionDeUsuario(request.POST)
    if formulario.is_valid():
        formulario.save()
        return redirect("inicio")
    return render(request, "registrar.html", {"formulario":formulario})
# Create your views here.

def perfil(request):
    return render(request, "perfil.html")

def editar_perfil(request):
    
    user = request.user
    datos_extra, _ = DatosExtras.objects.get_or_create(user=user)
    
    if request.method == "POST":
        formulario = EditarPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                datos_extra.avatar = avatar
                 
            datos_extra.save()
            formulario.save()
            return redirect('inicio')
    else:
        formulario = EditarPerfil(initial={'avatar': datos_extra.avatar}, instance=request.user)
    return render(request, 'editar_perfil.html', {'formulario': formulario})
