from django.urls import path
from .import views as v

app_name="personas"

urlpatterns = [

    #URLS Clientes
    path('clientes/',v.index_personas.as_view(),name="indexCliente"),
    path('clientes/nuevo/',v.ClienteCreateView.as_view(),name="crearCliente"),
    path('clientes/detalles/<pk>/',v.ClienteDetailView.as_view(),name="detalleCliente"),
    path('clientes/actualizar/<pk>/',v.ClienteUpdateView.as_view(),name="actualizarCliente"),
    path('clientes/eliminar/<pk>/',v.ClienteDeleteView.as_view(),name="eliminarCliente"),

    #URLS Proveedores
    path('proveedores/',v.ProveedorListView.as_view(),name="indexProveedor"),
    path('proveedores/nuevo',v.ProveedorCreateView.as_view(),name="crearProveedor"),
    path('proveedores/detalles/<pk>/',v.ProveedorDetailView.as_view(),name="detalleProveedor"),
    path('proveedores/actualizar/<pk>/',v.ProveedorUpdateView.as_view(),name="actualizarProveedor"),
    path('proveedores/eliminar/<pk>/',v.ProveedorDeleteView.as_view(),name="eliminarProveedor"),
]
