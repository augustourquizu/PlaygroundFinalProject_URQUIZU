# Generated by Django 5.0.3 on 2024-03-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0011_alter_lista_datos_extra_alter_lista_dia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='datos_extra',
            field=models.CharField(default='Nombre por ej.', max_length=50),
        ),
    ]
