from django.contrib import admin
from .models import Usuario, Vehiculo, LugarParqueo, Suscripcion

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(LugarParqueo)