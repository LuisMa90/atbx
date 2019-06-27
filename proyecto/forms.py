from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import *


class PromoventeForm(forms.ModelForm):

    class Meta:
        model = Promovete
        fields = ['promovente', 'rfc', 'representante']
        widgets = {
            'promovente':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre del promovente'}),
            'rfc':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Registro Federal del Contribuyente'}),
            'representante':forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre del Representante Legal'}),
        }


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['cliente', 'rfc', 'ubicacion', 'promovente']
        widgets = {
            'cliente':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre o razón social del cliente'
                }),
            'rfc':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Registro Federal del Contribuyente'
                }),
            'ubicacion':
            forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ubicación del cliente'
            }),
            'promovente':forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Promovente del cliente'
            }),
        }


class TipoServicioForm(forms.ModelForm):
    class Meta:
        model = TipoServicios
        fields = ['nombre', 'desc']
        widgets = {
            'nombre':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del tipo de servicio'
                }),
            'desc':
            forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripcion de las tareas del servicio'
                }),
        }


class TipoProyectoForm(forms.ModelForm):
    class Meta:
        model = TipoProyecto
        fields = ['nombre', 'desc']
        widgets = {
            'nombre':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del tipo de proyecto'
                }),
            'desc':
            forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Que tareas tiene el proyecto'
                }),
        }

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = [
            'nombre', 'fecha_de_inicio', 'fecha_de_entrega',
            'tipo_de_servicio', 'capacidad', 'responsable', 'tarea'
        ]
        widgets = {
            'nombre':
            forms.TextInput(
                attrs={
                    'class':
                    'form-control',
                    'placeholder':
                    'Nombre del tipo servicio a ofrecer ejemplo 13/01/2018'
                }),
            'fecha_de_inicio':
            forms.DateInput(
                attrs={
                    'class':
                    'form-control',
                    'placeholder':
                    'Cual es la fecha de inicio del servicio 13/01/2018'
                }),
            'fecha_de_entrega':
            forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Cual es la fecha de entrega del servicio'
                }),
            'tipo_de_servicio':
            forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Que tipo de Servicio se ofrecera'
                }),
            'capacidad':
            forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Que capacidad tendra el servicio'
                }),
            'responsable':
            forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Quien sera el responsable del servicio'
                }),
            'tarea':
            forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Que tareas se realizaran'
            }),
        }

class ProeyctoForm(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = [
            'nombre', 'promoventes', 'cliente', 'fecha_de_inicio',
            'tipo_de_proyecto', 'auto', 'superficie', 'estudios',
            'responsable', 'descripcion'
        ]
        widgets = {
            'nombre':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del proyecto a desarrollar'
                }),
            'promoventes':
            forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del promovente del proyecto'
                }),
            'cliente':
            forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del cliente del proyecto'
                }),
            'fecha_de_inicio':
            forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Fecha de inicio del proyecto ej 01/09/2017'
                }),
            'tipo_de_proyecto':
            forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Fecha de inicio del proyecto ej 01/09/2017'
                }),
            'auto':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Autorización del proyecto'
                }),
            'superficie':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Superficie que abarca el proyecto'
                }),
            'superficie':
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Superficie que abarca el proyecto'
                }),
            'estudios':
            forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Estudios o servicios del proyecto'
                }),
            'responsable':
            forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Responsable del proyectp'
                }),
            'descripcion':
            forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Descripcion del proyecto'
                }),
        }