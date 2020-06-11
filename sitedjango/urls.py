#from django.contrib import admin
from django.urls import path
from .views import *
from sitedjango import views

urlpatterns = [
    path('', views.home), 
    path('formulario/', views.formulario), 
    path('sobre/', views.sobre),
    path('servicos/', views.servicos),
    path('formulario/insereFormulario', views.insereFormulario), 
    
]