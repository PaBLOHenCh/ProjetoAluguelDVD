from django.urls import path
from . import views

urlpatterns = [
    path('', views.adicionar_dvd, name="adicionar-dvd"),
    path('aluguel/', views.remover_dvd, name="remover-dvd"),
    path('delete/', views.deletar_dvd, name="deletar-dvd"),
]