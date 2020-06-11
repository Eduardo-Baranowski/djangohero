# Generated by Django 2.2.13 on 2020-06-11 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='name')),
                ('datanascimento', models.DateTimeField(auto_now=True, verbose_name='dataNascimento')),
                ('naturalidade', models.CharField(max_length=150, verbose_name='naturalidade')),
                ('cpf', models.CharField(max_length=11, verbose_name='cpf')),
                ('rg', models.CharField(max_length=20, verbose_name='rg')),
                ('dataRg', models.DateTimeField(auto_now=True, verbose_name='datarg')),
                ('orgaoEmissor', models.CharField(max_length=11, verbose_name='orgaoemissor')),
                ('estadoCivil', models.CharField(max_length=20, verbose_name='estadocivil')),
                ('nomeMae', models.TextField(max_length=150, verbose_name='nomemae')),
                ('email', models.EmailField(max_length=150, verbose_name='email')),
                ('celular', models.CharField(max_length=50, verbose_name='celular')),
                ('telefoneResidencial', models.CharField(max_length=50, verbose_name='residencial')),
                ('telefoneComercial', models.CharField(max_length=50, verbose_name='residencial')),
                ('profissao', models.CharField(max_length=150, verbose_name='profissao')),
                ('renda', models.CharField(max_length=150, verbose_name='renda')),
                ('empresa', models.CharField(max_length=150, verbose_name='empresa')),
                ('cep', models.CharField(max_length=20, verbose_name='cep')),
                ('estado', models.CharField(max_length=20, verbose_name='estado')),
                ('cidade', models.CharField(max_length=20, verbose_name='cidade')),
                ('bairro', models.CharField(max_length=20, verbose_name='bairro')),
                ('rua', models.CharField(max_length=20, verbose_name='rua')),
                ('nuemero', models.CharField(max_length=20, verbose_name='numero')),
                ('complemento', models.CharField(max_length=150, verbose_name='complemento')),
            ],
        ),
    ]
