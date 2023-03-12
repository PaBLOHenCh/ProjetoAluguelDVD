from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes, name="clientes"),
    path('cadastro_cliente/', views.cadastro_cliente, name='cadastro-cliente'),
    path('login/', views.login, name = 'login-cliente'),
    path('dvds_alugados/', views.dvds_alugados, name='dvds-alugados'),
]