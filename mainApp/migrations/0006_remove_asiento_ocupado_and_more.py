# Generated by Django 5.1.1 on 2024-12-09 00:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_ventas_asientos_seleccionados_asiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asiento',
            name='ocupado',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='asientos_seleccionados',
        ),
        migrations.AddField(
            model_name='asiento',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='asiento',
            name='fila',
            field=models.CharField(default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='ventas',
            name='asientos',
            field=models.ManyToManyField(related_name='ventas', to='mainApp.asiento'),
        ),
        migrations.AlterField(
            model_name='asiento',
            name='funcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.funcion'),
        ),
        migrations.AlterField(
            model_name='asiento',
            name='numero',
            field=models.PositiveIntegerField(),
        ),
    ]