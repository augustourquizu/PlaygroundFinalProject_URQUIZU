# Generated by Django 5.0.3 on 2024-03-13 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
