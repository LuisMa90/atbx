from django.urls import path
from .views import MapsView

maps_patterns = ([
    path('', MapsView.as_view(), name='maps'),
    
], 'maps')
    