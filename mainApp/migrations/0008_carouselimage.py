# Generated by Django 5.1.1 on 2024-12-09 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_remove_ventas_asientos_delete_asiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Título de la imagen', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Descripción corta (opcional)')),
                ('image', models.ImageField(help_text='Sube la imagen para el carrusel', upload_to='carousel/')),
                ('order', models.PositiveIntegerField(default=0, help_text='Orden de la imagen en el carrusel')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]