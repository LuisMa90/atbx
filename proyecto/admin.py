from django.contrib import admin
from .models import *

class PromoAdmin(admin.ModelAdmin):
    list_display = ('promovente','rfc')

    class Media:
        css = {
            'all': ('proyecto/css/custom_ckeditor.css', )
        }

class ProyectAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_de_proyecto')

    class Media:
        css = {'all': ('proyecto/css/custom_ckeditor.css', )}


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_de_servicio')

    class Media:
        css = {'all': ('proyecto/css/custom_ckeditor.css', )}


class ClientAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'rfc')

    class Media:
        css = {'all': ('proyecto/css/custom_ckeditor.css', )}


class TypeProAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

    class Media:
        css = {'all': ('proyecto/css/custom_ckeditor.css', )}


class TypeServiceAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

    class Media:
        css = {'all': ('proyecto/css/custom_ckeditor.css', )}



admin.site.register(Promovete,PromoAdmin)
admin.site.register(Proyectos,ProyectAdmin)
admin.site.register(Servicios,ServiceAdmin)
admin.site.register(Cliente,ClientAdmin)
admin.site.register(TipoProyecto,TypeProAdmin)
admin.site.register(TipoServicios,TypeServiceAdmin)
