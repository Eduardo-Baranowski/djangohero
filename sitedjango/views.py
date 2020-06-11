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

def insereFormulario(request):
    # conexão com os servidores do google
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
    # username ou email para logar no servidor
    username = 'eduardobaranowskiteste@gmail.com'
    password = '12345678br'

    from_addr = 'cahwski@gmail.com'
    to_addrs = ['cahwski@gmail.com']
    # a biblioteca email possuí vários templates
    # para diferentes formatos de mensagem
    # neste caso usaremos MIMEText para enviar
    # somente texto
    message = MIMEText('Hello World')
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