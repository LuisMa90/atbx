from django.shortcuts import render
#ReportLab
from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from django.http import FileResponse
#Vistas
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required  #para importar el metodo de la validacion con decoreacion
from django.utils.decorators import method_decorator  #para importar el metodo de decoracion de clases
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
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
#vistas de los vehiculos
class ListVehiculo(ListView):
    model = Vehiculos


@method_decorator(staff_member_required, name='dispatch')
#Vistas de las actividades
class ListActividades(ListView):
    model = Actividad



#vistas de los reportes diarios

@method_decorator(staff_member_required, name='dispatch')
class ListDiario(ListView):
    model = Diario
    paginate_by = 10


@method_decorator(staff_member_required, name='dispatch')
class DiarioDetailView(DetailView):
    model = Diario



@method_decorator(staff_member_required, name='dispatch')
class CreateDiario(CreateView):
    model = Diario
    form_class = DiarioForm
    success_url = reverse_lazy('reporte:ReporteDiario')

    def get_context_data(self, **kwargs):#Para poder manejar los formularios osea agregados en el html
        context = super(CreateDiario, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context


@method_decorator(staff_member_required, name='dispatch')
class updateDiario(UpdateView):
    model = Diario
    form_class = DiarioForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('reporte:ReporteDiario')


@method_decorator(staff_member_required, name='dispatch')
class delateReporteDiario(DeleteView):
    model = Diario
    success_url = reverse_lazy('reporte:ReporteDiario')
