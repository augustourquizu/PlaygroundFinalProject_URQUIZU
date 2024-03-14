from django.urls import path
from lista.views import Evento, EditarElemento, CrearElemento, DetalleElemento, EliminarElemento

urlpatterns = [
    path('evento/', Evento.as_view(), name='evento'),
    path('evento/nuevo/', CrearElemento.as_view(), name='crear_elemento'),
    path('evento/<int:pk>/', DetalleElemento.as_view(), name='detalle_elemento'),
    path('evento/<int:pk>/editar/', EditarElemento.as_view(), name='editar_elemento'),
    path('evento/<int:pk>/eliminar/', EliminarElemento.as_view(), name='eliminar_elemento'),
]