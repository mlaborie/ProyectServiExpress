# Generated by Django 4.2.6 on 2023-11-25 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServiExpress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordendecompra',
            name='id_proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ServiExpress.proveedor'),
        ),
    ]
