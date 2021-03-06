# Generated by Django 4.0.4 on 2022-06-04 21:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App_Control_Parking', '0004_rename_placa_vehiculo_placa_vehiculo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='fecha_entrada',
        ),
        migrations.AddField(
            model_name='lugarparqueo',
            name='documento_usuario',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='lugarparqueo',
            name='fecha_entrada',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='lugarparqueo',
            name='fecha_salida',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='lugarparqueo',
            name='placa_vehiculo_asignado',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='lugarparqueo',
            name='precio_minuto',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='typology_lugar',
            field=models.ManyToManyField(blank=True, related_name='lugar', to='App_Control_Parking.lugarparqueo'),
        ),
    ]
