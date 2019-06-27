from django.shortcuts import render
from .forms import NaturalFrom
import requests
from django.http import JsonResponse, HttpResponse

import json 

# Create your views here.
#def natural(request):
 #   response = requests.get('http://api.inaturalist.org/v1/observations?nelat=37.234&nelng=-91.079&swlat=27.024&swlng=-102.790&order=desc&order_by=created_at')
  #  results = response.json()
   # return render(request, 'natural/natural.html',
    #              {
     #               'results': results['results']       
      #             })  #este es el codigo para mostrar el resultado y el json


def natural(request):
    search_result = {}
    if 'nelat' in request.GET and 'nelng' in request.GET and 'swlat' in request.GET and 'swlng' in request.GET:
        print("si entra en este if")
        form = NaturalFrom(request.GET)
        if form.is_valid():
            search_result = form.search()
            
            print("si entra en este if")
    else:
        form = NaturalFrom()
        print("aqui no debe de entrar")

    
    return render(request, 'natural/natural.html', {'form': form, 'search_result': search_result})
