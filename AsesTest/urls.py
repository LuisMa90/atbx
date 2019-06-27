"""webplayground URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from maps.urls import maps_patterns
from proyecto.urls import proyecto_patterns
from reporte.urls import reporte_patterns
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),
    path('pages/', include(pages_patterns)),
    path('admin/', admin.site.urls),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Paths de profiles
    path('profiles/', include(profiles_patterns)),
    # Paths de Messenger
    path('messenger/', include(messenger_patterns)),
    #Paths de los maps
    path('maps/',include(maps_patterns)),
    #Paths de inatural
    path('natural/',include('natural.urls')),
    #Path de los proyectos
    path('proyecto/',include(proyecto_patterns)),
    #Path de los reportes
    path('reporte/',include(reporte_patterns)),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Perzonalizacion del admin
admin.site.site_header = "Administracion de Toolbox Ases"
admin.site.index_title = "Panel de administrador"
admin.site.site_title = "Administracion Ases"