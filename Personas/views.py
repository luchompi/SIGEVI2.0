from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.edit import DeleteView
from .models import Cliente
from .forms import clienteForm
from django.views.generic import ListView,CreateView,DetailView,UpdateView
# Create your views here.


class index_personas(PermissionRequiredMixin,ListView):
    permission_required="Personas.view_cliente"
    template_name = "Personas/index.html"
    model = Cliente
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consulta=self.request.GET.get('identificacion')
        if consulta:
            context["query"] = Cliente.objects.filter(identificacion__istartswith=consulta)
        else:
            context["query"] = Cliente.objects.all()
        return context



class ClienteCreateView(PermissionRequiredMixin,CreateView):
    permission_required = "Personas.add_cliente"
    model = Cliente
    form = clienteForm
    fields =[
        'identificacion',
        'nombre',
        'apellido',
        'direccion',
        'telefono',
        'correo',
    ]
    template_name = "Personas/create.html"
    success_url = '/personas/clientes/'


class ClienteDetailView(PermissionRequiredMixin,DetailView):
    permission_required="Personas.view_cliente"
    model = Cliente
    template_name = "Personas/detail.html"


class ClienteUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = "Personas.change_cliente"
    model = Cliente
    form = clienteForm
    fields =[
        'nombre',
        'apellido',
        'direccion',
        'telefono',
        'correo',
    ]
    template_name = "Personas/update.html"
    success_url = "/personas/clientes/detalles/{identificacion}"


class ClienteDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = "Personas.delete_cliente"
    model = Cliente
    template_name = "Personas/delete.html"
    success_url= "/personas/clientes/"

