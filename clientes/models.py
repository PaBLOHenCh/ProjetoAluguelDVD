from dvds.models import DVD
from django.db import models
from django.contrib.auth.models import AbstractUser


# class clientes(AbstractUser):
#     choices_perfil = (('C', 'Cliente'), ('F', 'Funcionario'))
#     perfil = models.CharField(max_length=1, choices = choices_perfil)
#     dvds = models.ManyToManyField(DVD)
    
#     def __str__(self) -> str:
#         return self.username
