from django.urls import path
from . import views
from usuarios.views import registrar
urlpatterns = [ path("registrar/", registrar, name='registrar')
]
