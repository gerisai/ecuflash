# Generated by Django 4.0.1 on 2022-01-19 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.imagen'),
        ),
    ]
