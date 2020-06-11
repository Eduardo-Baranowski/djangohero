from django.db import models
from django import forms

# Create your models here.


class Formulario(models.Model):    
    nome = models.CharField('name', max_length=150)
    datanascimento = models.DateTimeField('dataNascimento',auto_now=True)
    naturalidade = models.CharField('naturalidade', max_length=150)    
    cpf = models.CharField('cpf', max_length=11)    
    rg = models.CharField('rg', max_length=20)    
    dataRg = models.DateTimeField('datarg',auto_now=True)
    orgaoEmissor = models.CharField('orgaoemissor', max_length=11)    
    estadoCivil = models.CharField('estadocivil', max_length=20)    
    nomeMae = models.TextField('nomemae', max_length=150)
    email = models.EmailField('email', max_length=150)
    celular = models.CharField('celular', max_length=50)    
    telefoneResidencial = models.CharField('residencial', max_length=50)    
    telefoneComercial = models.CharField('comercial', max_length=50)    
    profissao = models.CharField('profissao', max_length=150)
    renda = models.CharField('renda', max_length=150)
    empresa = models.CharField('empresa', max_length=150)
    cep = models.CharField('cep', max_length=20)
    estado = models.CharField('estado', max_length=20)
    cidade = models.CharField('cidade', max_length=20)
    bairro = models.CharField('bairro', max_length=20)
    rua = models.CharField('rua', max_length=20)
    nuemero = models.CharField('numero', max_length=20)
    complemento = models.CharField('complemento', max_length=150)
    

    def __str__(self):
        return self.nome