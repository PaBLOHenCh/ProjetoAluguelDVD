from django.db import models
from usuarios.models import Users
from datetime import datetime


class DVD(models.Model):
    titulo = models.CharField(max_length=50)
    sinopse = models.CharField(max_length=500)
    quantidade = models.IntegerField(default=1)
    caminho_imagem = models.CharField(max_length=500, default='../templates/static/dvds/img/default.png')
    lista_espera_dvd = models.CharField(max_length=255)
    
    
    def __str__(self) -> str:
        return self.titulo

class aluguel(models.Model):
    id_cliente = models.ForeignKey(Users, on_delete=models.CASCADE)
    id_dvd = models.ForeignKey(DVD, on_delete=models.CASCADE)
    aluguel_dvd_pago = models.BooleanField(default=False)
    data_aluguel = models.DateTimeField(default= datetime.now()) 
    valor_aluguel = models.FloatField(default= 0.0)
    nome = models.CharField(max_length=255)
    lista = []
    
    def __str__(self) -> str:
        return self.nome
    
class lista_espera(models.Model):
    dvd = models.ForeignKey(DVD, on_delete= models.CASCADE)
    cliente = models.ForeignKey(Users, on_delete= models.CASCADE)
    nome = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.nome
    
