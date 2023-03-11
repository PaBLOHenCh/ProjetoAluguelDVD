from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from rolepermissions.decorators import has_permission_decorator
from dvds.models import DVD


@has_permission_decorator('home_funcionarios')
def home (request):
    return render(request, 'home_funcionarios.html')


@has_permission_decorator('consulta_funcionarios')
def consulta(request):
    lista = DVD.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request, 'estoque.html', context)