from django.urls import path
from .import views as v

app_name="personas"

urlpatterns = [
    path('clientes/',v.index_personas.as_view(),name="indexCliente"),
    path('clientes/nuevo/',v.ClienteCreateView.as_view(),name="crearCliente"),
    path('clientes/detalles/<pk>/',v.ClienteDetailView.as_view(),name="detalleCliente"),
    path('clientes/actualizar/<pk>/',v.ClienteUpdateView.as_view(),name="actualizarCliente"),
    path('clientes/eliminar/<pk>/',v.ClienteDeleteView.as_view(),name="eliminarCliente"),
]
