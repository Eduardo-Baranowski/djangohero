# Generated by Django 2.2.13 on 2020-06-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitedjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='telefoneComercial',
            field=models.CharField(max_length=50, verbose_name='comercial'),
        ),
    ]
