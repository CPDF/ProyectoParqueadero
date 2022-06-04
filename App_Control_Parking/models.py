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

class LugarParqueo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo_lugar = models.CharField(default='', max_length=1000)
    placa_vehiculo_asignado = models.CharField(default='', max_length=1000)
    documento_usuario = models.CharField(default='', max_length=1000)
    fecha_entrada = models.DateTimeField(default=now, blank=True)
    ocupado = models.BooleanField(default=False)


    def __str__(self):
        return self.codigo_lugar


# Create your models here.
class Vehiculo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    placa_vehiculo = models.CharField(default='', max_length=1000)
    documento_usuario = models.CharField(default='', max_length=1000)
    modelo = models.CharField(default='', max_length=10)
    typology = models.ManyToManyField(
    Usuario,
    blank=True,
    related_name='usuario'
)
    typology_lugar = models.ManyToManyField(
    LugarParqueo,
    blank=True,
    related_name='lugar'
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

