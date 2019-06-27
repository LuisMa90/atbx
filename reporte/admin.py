from django.contrib import admin
from .models import *


class DiarioAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'servicio', 'actividad')

    


admin.site.register(Actividad)
admin.site.register(Vehiculos)
admin.site.register(Diario,DiarioAdmin)
