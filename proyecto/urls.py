from django.urls import path
from .views import *

proyecto_patterns = (
    [
        #path de los promoventes
        path('promovente/', Promovente_list.as_view(), name='promovente'),
        path(
            'promovente/create/',
            NewPromovete.as_view(),
            name='promovente_create'),
        path(
            'promovente/update/<int:pk>',
            updatePromovete.as_view(),
            name='promovente_update'),
        path(
            'promovente/delate/<int:pk>',
            delatePromovete.as_view(),
            name='promovente_delete'),
        #path de los clientes
        path('clientes/', ClienteList.as_view(), name='clientes'),
        path('clientes/create/', NewCliente.as_view(), name='cliente_create'),
        path('clientes/update/<int:pk>',updateCliente.as_view(),name='cliente_update'),
        path('clientes/delate/<int:pk>',delateCliente.as_view(),name='cliente_delete'),
        #Path de los tipos de servicios

        path('TipoServicios/', TSList.as_view(), name='ts'),
        path('TipoServicios/create/', NewTS.as_view(), name='ts_create'),
        path('TipoServicios/update/<int:pk>',updateTS.as_view(),name='ts_update'),
        path('TipoServicios/delate/<int:pk>',delateTS.as_view(),name='ts_delete'),

        #Path de los tipos de proyectos
        path('TipoProyectos/', TpList.as_view(), name='tp'),
        path('TipoProyectos/create/', NewTp.as_view(), name='tp_create'),
        path('TipoProyectos/update/<int:pk>',updateTp.as_view(),name='tp_update'),
        path('TipoProyectos/delate/<int:pk>',delateTp.as_view(),name='tp_delete'),

        #Path de los servicios
        path('Servicios/', ServiciosList.as_view(), name='servicios'),
        path('Servicios/create/', NewServicio.as_view(), name='servicios_create'),
        path('Servicios/update/<int:pk>',updateServicio.as_view(),name='servicios_update'),
        path('Servicios/delate/<int:pk>',delateServicios.as_view(),name='servicios_delete'),

        #path de los proyectos
         path('', ProyectosList.as_view(), name='proyectos'),
         path('create/', NewProyecto.as_view(), name='proyecto_create'),
        path('update/<int:pk>',updateProyecto.as_view(),name='proyectos_update'),
        path('delate/<int:pk>',delateProyectos.as_view(),name='proyectos_delete'),
    ],
    'proyecto')
