# Generated by Django 2.2.2 on 2019-07-04 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_auto_20190704_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='precio',
            field=models.FloatField(default=0.0, verbose_name='Precio'),
        ),
    ]
