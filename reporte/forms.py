import datetime
from django import forms
from django.contrib.admin import widgets
from django.forms.fields import DateField
from django.forms.widgets import SelectDateWidget

from django.contrib.admin.widgets import AdminDateWidget
from .models import *


class DiarioForm(forms.ModelForm):
    class Meta:
        model = Diario
        fields = [
            'fecha',
            'proyecto',
            'inicio_jornada',
            'termino_jornada',
            'no_vehiculo',
            'modelos_vehiculos',
            'servicio',
            'responsable',
            'supervisor',
            'no_coordi',
            'coordinadores',
            'no_especialistas',
            'especialistas',
            'no_tec',
            'tecnicos',
            'actividad',
            'desc',
            'img',
            'act_1',
            'desc_1',
            'img_1',
            'act_2',
            'desc_2',
            'img_2',
            'act_3',
            'desc_3',
            'img_3',
            'act_4',
            'desc_4',
            'img_4',
            'act_5',
            'desc_5',
            'img_5',
            'act_6',
            'desc_6',
            'img_6',
            'act_7',
            'desc_7',
            'img_7',
            'act_8',
            'desc_8',
            'img_8',
            'act_9',
            'desc_9',
            'img_9',
        ]
        widgets = {
            'fecha':
            forms.SelectDateWidget(attrs={
                'class': 'form-control ',
                'placeholder': 'Fecha del reporte'
            }),
            'proyecto':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Proyecto del cual sera el reporte'
                }),
            'inicio_jornada':
            forms.TextInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Ejemplo 09:30:00'
            }),
            'termino_jornada':
            forms.TimeInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Ejemplo 19:30:00'
            }),
            'no_vehiculo':
            forms.NumberInput(attrs={
                'class': 'form-control ',
                'placeholder': 'Cantidad de vehiculos'
            }),
            'modelos_vehiculos':
            forms.SelectMultiple(attrs={
                'class': 'form-control ',
                'placeholder': 'Fin de la jornada'
            }),
            'servicio':
            forms.Select(attrs={
                'class': 'form-control ',
                'placeholder': 'Servicio a reportar'
            }),
            'responsable':
            forms.Select(attrs={
                'class': 'form-control ',
                'placeholder': 'Responsable en sitio '
            }),
            'supervisor':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Supervisor de seguridad y ambiente'
                }),
            'no_coordi':
            forms.NumberInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de coordinadores en el proyecto'
                }),
            'coordinadores':
            forms.SelectMultiple(
                attrs={
                    'class':
                    'form-control ',
                    'placeholder':
                    'Coordinadores del proyecto, si son 2 o mas selecciona con clic y la tecla ctrl'
                }),
            'no_especialistas':
            forms.NumberInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de especialistas en el proyecto'
                }),
            'especialistas':
            forms.SelectMultiple(
                attrs={
                    'class':
                    'form-control ',
                    'placeholder':
                    'Especialistas del proyecto, si son 2 o mas selecciona con clic y la tecla ctrl'
                }),
            'no_tec':
            forms.NumberInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'tecnicos':
            forms.SelectMultiple(
                attrs={
                    'class':
                    'form-control ',
                    'placeholder':
                    'Tecnicos del proyecto, si son 2 o mas selecciona con clic y la tecla ctrl'
                }),
            'actividad':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'desc':
            forms.Textarea(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'img':
            forms.ClearableFileInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'act_1':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'desc_1':
            forms.Textarea(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'img_1':
            forms.ClearableFileInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'act_2':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'desc_2':
            forms.Textarea(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'img_2':
            forms.ClearableFileInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'act_3':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'desc_3':
            forms.Textarea(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'img_3':
            forms.ClearableFileInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'act_4':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'desc_4':
            forms.Textarea(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'img_4':
            forms.ClearableFileInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'act_5':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'desc_5':
            forms.Textarea(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'img_5':
            forms.ClearableFileInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'act_6':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'desc_6':
            forms.Textarea(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'img_6':
            forms.ClearableFileInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'act_7':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'desc_7':
            forms.Textarea(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'img_7':
            forms.ClearableFileInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'act_8':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'desc_8':
            forms.Textarea(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'img_8':
            forms.ClearableFileInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'act_9':
            forms.Select(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'desc_9':
            forms.Textarea(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
            'img_9':
            forms.ClearableFileInput(
                attrs={
                    'class': 'form-control ',
                    'placeholder': 'Numero de tecnicos en el proyecto'
                }),
        }
