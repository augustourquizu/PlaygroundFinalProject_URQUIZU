# Generated by Django 5.0.3 on 2024-03-14 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0016_alter_lista_datos_extra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lista',
            name='datos_extra',
        ),
        migrations.AddField(
            model_name='lista',
            name='nombre',
            field=models.CharField(default='', max_length=50),
        ),
    ]