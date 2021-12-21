from django.urls import path 
from . import views as v
app_name="producto"
urlpatterns = [
    


    #Gestion de Productos
    path('',v.ProductoList.as_view(),name="productoIndex"),
    path('nuevo/',v.ProductoCreate.as_view(),name="productoCrear"),
    path('detalles/<pk>/',v.ProductoDetail.as_view(),name="productoDetalle"),
    path('actualizar/<pk>/',v.ProductoUpdate.as_view(),name="productoEditar"),
    path('eliminar/<pk>/',v.ProductoDelete.as_view(),name="productoEliminar"),
    path('related/<categoria>/',v.ProductoCategoria,name="productoCategoria"),


    #carrito
    path('agregar/<pk>/',v.agregar_carrito,name="add"),
    path('eliminar/<pk>/',v.eliminar_producto,name="del"),
    path('restar/<pk>/',v.restar_producto,name="remove"),
    path('limpiar/',v.limpiar,name="cls"),
    path('pay/',v.pagar,name="pay"),
    path('PDF/', v.generar_pdf, name="PDF"),

]
