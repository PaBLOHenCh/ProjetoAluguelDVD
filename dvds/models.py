from django.db import models

class DVD(models.Model):
    titulo = models.CharField(max_length=50)
    sinopse = models.CharField(max_length=500)
    quantidade = models.IntegerField(default=1)
    caminho_imagem = models.CharField(max_length=500, default='../templates/static/dvds/img/default.png')
    
    def __str__(self) -> str:
        return self.titulo
