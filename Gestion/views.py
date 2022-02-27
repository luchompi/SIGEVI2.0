from .models import Marca,Categoria
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from Gestion.froms import marcaForm,categoriaForm

class MarcaList(PermissionRequiredMixin,ListView):
	permission_required = "Gestion.view_marca"
	model = Marca
	template_name = "Marca/index.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		if consulta := self.request.GET.get('marca'):
			context["query"] = Marca.objects.filter(nombre__istartswith=consulta)
		else:
			context["query"]= Marca.objects.all()
		return context



class MarcaCreate(PermissionRequiredMixin,CreateView):
	permission_required = "Gestion.add_marca"
	model = Marca
	form = marcaForm
	fields=['nombre',]
	template_name = "Marca/create.html"
	success_url = '/gestion/marca/'


class MarcaUpdate(PermissionRequiredMixin,UpdateView):
	permission_required = "Gestion.change_marca"
	model = Marca
	template_name = "Marca/update.html"
	form = marcaForm
	fields=['nombre',]
	success_url = '/gestion/marca/'



class MarcaDelete(PermissionRequiredMixin,DeleteView):
	permission_required = "Gestion.delete_marca"
	model = Marca
	template_name = "Marca/delete.html"
	success_url = '/gestion/marca/'


class CategoriaList(PermissionRequiredMixin,ListView):
    permission_required = "Gestion.view_categoria"
    model = Categoria
    template_name = "Categoria/index.html"
    def get_context_data(self, **kwargs):
    	context = super().get_context_data(**kwargs)
    	if consulta := self.request.GET.get('categoria'):
    		context["query"] = Categoria.objects.filter(nombre__istartswith=consulta)
    	else:
    		context["query"] = Categoria.objects.all()
    	return context
    

class CategoriaCreate(PermissionRequiredMixin,CreateView):
    permission_required = "Gestion.add_categoria"
    model = Categoria
    form = categoriaForm
    fields=['nombre',]
    template_name = "Categoria/create.html"
    success_url = '/gestion/categoria/'


class CategoriaUpdate(PermissionRequiredMixin,UpdateView):
    permission_required = "Gestion.change_categoria"
    model = Categoria
    form = categoriaForm
    fields=['nombre',]
    template_name = "Categoria/update.html"
    success_url = '/gestion/categoria/'
 
class CategoriaDelete(PermissionRequiredMixin,DeleteView):
    permission_required = "Gestion.delete_categoria"
    model = Categoria
    template_name = "Categoria/delete.html"
    success_url = '/gestion/categoria/'

