# Generated by Django 4.1.3 on 2022-12-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMaturano', '0002_rename_fecha_compra_producto_fecha_remito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='fecha_remito',
            field=models.CharField(max_length=40),
        ),
    ]
