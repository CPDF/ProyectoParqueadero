import uuid
from django.db import models
from django.utils.timezone import now



# Create your models here.
class Vehiculo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    documento = models.CharField(default='', max_length=1000)
    placa = models.CharField(default='', max_length=1000)
    modelo = models.CharField(default='', max_length=10)

    def __str__(self):
        return self.documento

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    documento = models.CharField(default='', max_length=1000)
    nombres = models.CharField(default='', max_length=1000)
    correo = models.CharField(default='', max_length=100)
    telefono = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.documento

class Suscripcion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(default='', max_length=1000)
    tipo = models.CharField(default='', max_length=1000)
    documento_usuario = models.CharField(default='', max_length=10)

    def __str__(self):
        return self.documento_usuario

class Estadia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    placa = models.CharField(default='', max_length=1000)
    fecha = models.CharField(default='', max_length=1000)
    hora = models.CharField(default='', max_length=1000)
    precio = models.CharField(default='', max_length=1000)
    placa = models.CharField(default='', max_length=1000)
    estado = models.CharField(default='', max_length=1000)

    def __str__(self):
        return self.placa
