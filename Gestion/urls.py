from django.urls import path
from . import views as v

app_name="gestion"

urlpatterns=[
	#URLS marca
	path('marca/',v.MarcaList.as_view(),name="indexMarca"),
	path('marca/nuevo/',v.MarcaCreate.as_view(),name="crearMarca"),
	path('marca/editar/<pk>/',v.MarcaUpdate.as_view(),name="actualizarMarca"),
	path('marca/eliminar/<pk>/',v.MarcaDelete.as_view(),name="eliminarMarca"),

	#URLS CATEGORIA
	path('categoria/',v.CategoriaList.as_view(),name="indexCategoria"),
	path('categoria/nuevo',v.CategoriaCreate.as_view(),name="crearCategoria"),
	path('categoria/editar/<pk>',v.CategoriaUpdate.as_view(),name="actualizarCategoria"),
	path('categoria/eliminar/<pk>',v.CategoriaDelete.as_view(),name="eliminarCategoria"),

]