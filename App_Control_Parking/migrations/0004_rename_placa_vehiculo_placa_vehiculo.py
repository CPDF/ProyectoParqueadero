# Generated by Django 4.0.4 on 2022-05-18 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Control_Parking', '0003_lugarparqueo_delete_estadia_vehiculo_fecha_entrada_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiculo',
            old_name='placa',
            new_name='placa_vehiculo',
        ),
    ]
