import uuid
from django.db import models
from django.utils.timezone import now



class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    documento_usuario = models.CharField(default='', max_length=1000)
    nombres = models.CharField(default='', max_length=1000)
    correo = models.CharField(default='', max_length=100)
    telefono = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.documento_usuario

# Create your models here.
class Vehiculo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    placa_vehiculo = models.CharField(default='', max_length=1000)
    documento_usuario = models.CharField(default='', max_length=1000)
    modelo = models.CharField(default='', max_length=10)
    fecha_entrada = models.CharField(default='', max_length=1000)
    typology = models.ManyToManyField(
    Usuario,
    blank=True,
    related_name='usuario'
)
    def __str__(self):
        return self.documento_usuario

class Suscripcion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(default='', max_length=1000)
    tipo = models.CharField(default='', max_length=1000)
    documento_usuario = models.CharField(default='', max_length=10)

    def __str__(self):
        return self.documento_usuario

class LugarParqueo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_lugar = models.CharField(default='', max_length=1000)

    def __str__(self):
        return self.placa
