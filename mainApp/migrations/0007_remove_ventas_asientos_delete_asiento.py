# Generated by Django 5.1.1 on 2024-12-09 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_remove_asiento_ocupado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventas',
            name='asientos',
        ),
        migrations.DeleteModel(
            name='Asiento',
        ),
    ]
