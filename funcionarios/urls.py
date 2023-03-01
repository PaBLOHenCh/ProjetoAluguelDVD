from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_funcionarios"),
    path('consulta/', views.consulta, name="consulta-estoque")
]