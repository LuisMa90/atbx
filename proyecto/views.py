from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required  #para importar el metodo de la validacion con decoreacion
from django.utils.decorators import method_decorator  #para importar el metodo de decoracion de clases
from django.urls import reverse, reverse_lazy
from .models import *


class ValidacionStaff(object):
    """
    Este mixin requiere que el usuario sea miembo del staff
    """

    @method_decorator(staff_member_required)
    def dispatch(self, request, *arg, **kwargs):
        return super(ValidacionStaff, self).dispatch(request, *arg, **kwargs)


@method_decorator(staff_member_required, name='dispatch')
#Vistas de promovente
class Promovente_list(ListView):
    model = Promovete


@method_decorator(staff_member_required, name='dispatch')
class NewPromovete(CreateView):
    model = Promovete
    form_class = PromoventeForm
    success_url = reverse_lazy('proyecto:promovente')


@method_decorator(staff_member_required, name='dispatch')
class updatePromovete(UpdateView):
    model = Promovete
    form_class = PromoventeForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('proyecto:promovente')


@method_decorator(staff_member_required, name='dispatch')
class delatePromovete(DeleteView):
    model = Promovete
    success_url = reverse_lazy('proyecto:promovente')

#Vistas de clientes
@method_decorator(staff_member_required, name='dispatch')
class ClienteList(ListView):
    model = Cliente


@method_decorator(staff_member_required, name='dispatch')
class NewCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('proyecto:clientes')


@method_decorator(staff_member_required, name='dispatch')
class updateCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('proyecto:clientes')


@method_decorator(staff_member_required, name='dispatch')
class delateCliente(DeleteView):
    model = Cliente
    success_url = reverse_lazy('proyecto:clientes')

#Vistas de los tipos de servicios


@method_decorator(staff_member_required, name='dispatch')
class TSList(ListView):
    model = TipoServicios


@method_decorator(staff_member_required, name='dispatch')
class NewTS(CreateView):
    model = TipoServicios
    form_class = TipoServicioForm
    success_url = reverse_lazy('proyecto:ts')


@method_decorator(staff_member_required, name='dispatch')
class updateTS(UpdateView):
    model = TipoServicios
    form_class = TipoServicioForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('proyecto:ts')


@method_decorator(staff_member_required, name='dispatch')
class delateTS(DeleteView):
    model = TipoServicios
    success_url = reverse_lazy('proyecto:ts')

#Vistas de los tipos de proyecto
@method_decorator(staff_member_required, name='dispatch')
class TpList(ListView):
    model = TipoProyecto


@method_decorator(staff_member_required, name='dispatch')
class NewTp(CreateView):
    model = TipoProyecto
    form_class = TipoProyectoForm
    success_url = reverse_lazy('proyecto:tp')


@method_decorator(staff_member_required, name='dispatch')
class updateTp(UpdateView):
    model = TipoProyecto
    form_class = TipoProyectoForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('proyecto:tp')


@method_decorator(staff_member_required, name='dispatch')
class delateTp(DeleteView):
    model = TipoProyecto
    success_url = reverse_lazy('proyecto:tp')

#Vistas de los servicios
@method_decorator(staff_member_required, name='dispatch')
class ServiciosList(ListView):
    model = Servicios


@method_decorator(staff_member_required, name='dispatch')
class NewServicio(CreateView):
    model = Servicios
    form_class = ServicioForm
    success_url = reverse_lazy('proyecto:servicios')


@method_decorator(staff_member_required, name='dispatch')
class updateServicio(UpdateView):
    model = Servicios
    form_class = ServicioForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('proyecto:servicios')


@method_decorator(staff_member_required, name='dispatch')
class delateServicios(DeleteView):
    model = Servicios
    success_url = reverse_lazy('proyecto:servicios')

#Vistas de los proyectos
@method_decorator(staff_member_required, name='dispatch')
class ProyectosList(ListView):
    model = Proyectos


@method_decorator(staff_member_required, name='dispatch')
class NewProyecto(CreateView):
    model = Proyectos
    form_class = ProeyctoForm
    success_url = reverse_lazy('proyecto:proyectos')


@method_decorator(staff_member_required, name='dispatch')
class updateProyecto(UpdateView):
    model = Proyectos
    form_class = ProeyctoForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('proyecto:proyectos')


@method_decorator(staff_member_required, name='dispatch')
class delateProyectos(DeleteView):
    model = Proyectos
    success_url = reverse_lazy('proyecto:proyectos')