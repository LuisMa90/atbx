from django.urls import path
from .views import *

reporte_patterns = ([
    path('ReporteDiario/', ListDiario.as_view(), name='ReporteDiario'),
    path('ReporteDiario/<int:pk>/', DiarioDetailView.as_view(), name='reporte'),
    path('ReporteDiario/create/', CreateDiario.as_view(), name='ReporteDiario_create'),
    path('ReporteDiario/update/<int:pk>',updateDiario.as_view(),name='ReporteDiario_update'),
    path('ReporteDiario/delate/<int:pk>',delateReporteDiario.as_view(),name='ReporteDiario_delete'),
], 'reporte')
