from django.views.generic.list import ListView                              #para importar la calse de ListView
from django.views.generic.detail import DetailView                          #para importar la calse de DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView    #para importar la calse de la creacion, update y delet
from django.contrib.admin.views.decorators import staff_member_required     #para importar el metodo de la validacion con decoreacion
from django.utils.decorators import method_decorator                        #para importar el metodo de decoracion de clases
from django.urls import reverse, reverse_lazy                               #para importar el metodo de redirecionar invertida
from django.shortcuts import redirect                                       #para importar el metodo de redireccionar
from .models import Page                                                    #para importar el modelo a usar
from .forms import PageForm                                                 #para la form que vamos a utilizar para la validacion

class ValidacionStaff(object):
    """
    Este mixin requiere que el usuario sea miembo del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self,request,*arg,**kwargs):
        return super(ValidacionStaff,self).dispatch(request,*arg,**kwargs)

# Create your views here.
class PagesListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page


@method_decorator(staff_member_required, name = 'dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')


@method_decorator(staff_member_required, name = 'dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    

    def get_success_url(self):
        return reverse_lazy('pages:update',args=[self.object.id])+'?ok'

@method_decorator(staff_member_required, name = 'dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

    