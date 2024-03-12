from django.urls import path, re_path, include
from . import views
from usuarios.views import registrar, login, perfil, editar_perfil, EditarContrasenia
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [ path("registrar/", registrar, name='registrar'), 
               path("login/", login, name="login"),
               path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"), 
               path("perfil/", perfil, name='perfil'), 
               path("editar_perfil/", editar_perfil, name="editar_perfil"),
               path('cambiar_contrasenia/', views.EditarContrasenia.as_view(), name='cambiar_contrasenia'),
]