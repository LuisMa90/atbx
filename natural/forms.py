from django import forms
from django.conf import settings
import requests



class NaturalFrom(forms.Form):
    nelat = forms.FloatField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa la latitud en la cordenada noroeste',
                'label': 'Ingresa la latitud en la cordenada noroeste',
            }))
    nelng = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa la longitud en la cordenada noroeste'}))
    swlat = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa la latitud en la cordenada suroeste'}))
    swlng = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingresa la longitud en la cordenada suroeste'}))

    def search(self):
        result = {}
        nelat = self.cleaned_data['nelat']
        nelng = self.cleaned_data['nelng']
        swlat = self.cleaned_data['swlat']
        swlng = self.cleaned_data['swlng']
        endpoint = "http://api.inaturalist.org/v1/observations/species_counts?nelat={nelat}&nelng={nelng}&swlat={swlat}&swlng={swlng}"

        url = endpoint.format(
            nelat=nelat,
            nelng=nelng,
            swlat=swlat,
            swlng=swlng,
            )

        headers = {'api_header':'Accept: application/json'}
        response = requests.get(url, headers=headers)


        if response.status_code == 200:  # SUCCESS
            result = response.json()
            result['success'] = True
            print("si funciona la busqueda")
        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = 'Error en la busqueda '
                print("no funciona la busqueda")
            else:
                result[
                'message'] = 'La API de Inaturalis no se encuentra activa por el momento .'
        return result
