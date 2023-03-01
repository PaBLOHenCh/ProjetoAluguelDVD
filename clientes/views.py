from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from dvds.models import DVD


def clientes (request):
    lista = DVD.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request, 'clientes.html', context)