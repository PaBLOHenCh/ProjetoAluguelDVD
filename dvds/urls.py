from django.urls import path
from . import views

urlpatterns = [
    path('', views.adicionar_dvd, name="adicionar-dvd"),
    path('aluguel/', views.remover_dvd, name="remover-dvd"),
    path('delete/', views.deletar_dvd, name="deletar-dvd"),
    path('devolver_dvd/', views.devolver_dvd, name="devolver-dvd"),
    path('efetivar-pagamento-dvd/', views.efetivar_pagamento_dvd, name="efetivar-pagamento-dvd"),
    path('inserir_lista_espera/', views.inserir_lista_espera, name="inserir-lista-espera"),
]