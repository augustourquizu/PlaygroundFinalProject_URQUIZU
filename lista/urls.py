from django.urls import path
from lista.views import Lista, EditarElemento, CrearElemento, DetalleElemento, EliminarElemento

urlpatterns = [
    path('eventos/', Lista.as_view(), name='lista'),
    path('evento/nuevo/', CrearElemento.as_view(), name='crear_elemento'),
    path('evento/<int:pk>/', DetalleElemento.as_view(), name='detalle_elemento'),
    path('evento/<int:pk>/editar/', EditarElemento.as_view(), name='editar_elemento'),
    path('evento/<int:pk>/eliminar/', EliminarElemento.as_view(), name='eliminar_elemento'),
]