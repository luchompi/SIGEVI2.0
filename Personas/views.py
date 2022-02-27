from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import DeleteView
from .models import Cliente,Proveedor
from .forms import clienteForm,proveedorForm
from django.views.generic import ListView,CreateView,DetailView,UpdateView
# Create your views here.


class index_personas(PermissionRequiredMixin,ListView):
    permission_required="Personas.view_cliente"
    template_name = "Personas/index.html"
    model = Cliente
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('identificacion'):
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


#consulta de proveedores

class ProveedorListView(PermissionRequiredMixin,ListView):
    permission_required = "Personas.view_proveedor"
    model = Proveedor
    template_name = "Proveedor/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('NIT'):
            context["query"] = Proveedor.objects.filter(NIT__istartswith=consulta)
        else:
            context["query"] = Proveedor.objects.all()
        return context

class ProveedorCreateView(PermissionRequiredMixin,CreateView):
    permission_required = "Personas.add_proveedor"
    model = Proveedor
    form = proveedorForm
    fields =[
        'NIT',
        'razonSocial',
        'direccionEmpresa',
        'direccionVenta',
        'telefono',
        'correo'
        ]

    template_name = "Proveedor/create.html"
    success_url = '/personas/proveedores/'


class ProveedorDetailView(PermissionRequiredMixin,DetailView):
    permission_required="Personas.view_proveedor"
    model = Proveedor
    template_name = "Proveedor/detail.html"

class ProveedorUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = "Personas.add_proveedor"
    model = Proveedor
    form = proveedorForm
    fields =[
        'NIT',
        'razonSocial',
        'direccionEmpresa',
        'direccionVenta',
        'telefono',
        'correo'
        ]

    template_name = "Proveedor/update.html"
    success_url = "/personas/proveedores/detalles/{NIT}"



class ProveedorDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = "Personas.delete_proveedor"
    model = Proveedor
    template_name = "Proveedor/delete.html"
    success_url= "/personas/proveedores/"

