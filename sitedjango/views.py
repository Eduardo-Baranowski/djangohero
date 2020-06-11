from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import *
from django import forms
import smtplib
from email.mime.text import MIMEText

def home(request):
    return render(request, 'home.html')

def formulario(request):
    return render(request, 'formulario.html')

def planos(request):
    return render(request, 'planos.html')

def sobre(request):
    return render(request, 'sobre.html')

def servicos(request):
    return render(request, 'servicos.html')

def insereFormulario(request):
    # conexão com os servidores do google
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    # username ou email para logar no servidor
    username = 'eduardobaranowskiteste@gmail.com'
    password = '12345678br'
    from_addr = 'caroline.baranowski@autorizadoademilar.com.br'
    to_addrs = ['caroline.baranowski@autorizadoademilar.com.br']
    # a biblioteca email possuí vários templates
    # para diferentes formatos de mensagem
    # neste caso usaremos MIMEText para enviar
    # somente texto
    nome = request.POST.get('name')
    datanascimento = request.POST.get('dataNascimento')
    naturalidade = request.POST.get('naturalidade')
    cpf = request.POST.get('cpf')
    rg = request.POST.get('rg')
    datarg = request.POST.get('datarg')
    orgaoemissor = request.POST.get('orgaoemissor')
    estadocivil = request.POST.get('estadocivil')
    nomemae = request.POST.get('nomemae')
    email = request.POST.get('email')
    celular = request.POST.get('celular')
    residencial = request.POST.get('residencial')
    comercial = request.POST.get('comercial')
    profissao = request.POST.get('profissao')
    renda = request.POST.get('renda')
    empresa = request.POST.get('empresa')
    cep = request.POST.get('cep')
    estado = request.POST.get('estado')
    cidade = request.POST.get('cidade')
    bairro = request.POST.get('bairro')
    rua = request.POST.get('rua')
    numero = request.POST.get('numero')
    complemento = request.POST.get('complemento')
    message = MIMEText('Nome: '+nome+'\n'+'Data de Nascimento: '+ datanascimento+'\n'+'Naturalidade: '+naturalidade+'\n'+'Cpf: '+ cpf+'\n'+'rg '+rg+'\n'+'Data de Expedição do RG: ' + datarg+'\n'+'Orgão Emissor: '+ orgaoemissor+'\n'+'Estado Civil: '+estadocivil+'\n'+'Nome da Mãe: ' +nomemae+'\n'+'Email: '+email+'\n'+'Celular: '+celular+'\n'+'Telefone Residencial: '+residencial+'\n'+'Telefone Comercial: '+comercial+'\n'+'Profissão: ' + profissao+'\n'+'Renda: '+ renda+'\n'+'Empresa: '+empresa+'\n'+'Cep: '+cep+'\n'+'Estado: '+estado+'\n'+'Cidade: '+cidade + '\n'+'Bairro: '+ bairro + '\n'+'Rua: '+rua + '\n'+'Número: '+numero+'\n'+'Complemento: '+complemento)
    #message = MIMEText('Nome: '+nome+'\n'+'Data de Nascimento: '+ datanascimento+'\n'+'Naturalidade: '+naturalidade+'\n'+'Cpf: '+ cpf+'\n'+'rg '+rg+'\n'+'Data de Expedição do RG: ' + datarg)
    message['subject'] = 'Hello'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

    # conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    # para interagir com um servidor externo precisaremos
    # fazer login nele
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()
        
    return render(request, 'home.html')