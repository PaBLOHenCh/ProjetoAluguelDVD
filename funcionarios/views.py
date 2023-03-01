from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from dvds.models import DVD

def home (request):
    return render(request, 'home_funcionarios.html')

def consulta(request):
    lista = DVD.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request, 'estoque.html', context)