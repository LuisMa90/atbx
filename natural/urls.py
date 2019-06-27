from django.urls import path
from . import views

urlpatterns = [
    path('', views.natural, name='natural'),
]