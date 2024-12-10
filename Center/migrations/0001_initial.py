# Generated by Django 5.1.1 on 2024-12-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('titulo_pelicula', models.CharField(max_length=200)),
                ('texto_reclamo', models.TextField()),
                ('fecha_reclamo', models.DateTimeField(auto_now_add=True)),
                ('resuelto', models.BooleanField(default=False)),
            ],
        ),
    ]