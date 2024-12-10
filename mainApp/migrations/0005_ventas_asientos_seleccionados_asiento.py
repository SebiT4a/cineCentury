# Generated by Django 5.1.1 on 2024-12-08 23:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_remove_ventas_codigo_remove_ventas_funcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventas',
            name='asientos_seleccionados',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('ocupado', models.BooleanField(default=False)),
                ('funcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asientos', to='mainApp.funcion')),
            ],
        ),
    ]