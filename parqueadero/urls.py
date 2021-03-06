"""parqueadero URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from App_Control_Parking.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register_user/', GestionarUsuario.as_view(), name='register_user'),
    path('', Consultar.as_view(), name='consult'),
    path('register_vehicle/', GestionarEntradaVehiculo.as_view(), name='register_vehicle'),
    path('manage_user/<int:id>', GestionarUsuario.gestionar_usuario, name='manage_user'),
    path('checkout/<int:id>', GestionarSalidaVehiculo.as_view(), name='checkout'),
]
