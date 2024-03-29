# Generated by Django 2.2.2 on 2019-06-27 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_foto', models.CharField(blank=True, max_length=100)),
                ('foto', models.ImageField(blank=True, max_length=500, upload_to='media/imagenes_articulos', verbose_name='imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('foto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inicio.Foto')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('precio', models.FloatField(blank=True)),
            ],
        ),
    ]
