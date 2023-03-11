import asyncio
from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from .models import DVD
from django.http import HttpResponse
from django.db.models import F
from rolepermissions.decorators import has_permission_decorator
from .models import aluguel, lista_espera
from usuarios.models import Users
from django.contrib.auth.decorators import login_required

@has_permission_decorator('adicionar_dvd')
def adicionar_dvd(request):
    titulo = request.POST.get('titulo')
    sinopse = request.POST.get('sinopse')
    quantidade = request.POST.get('quantidade')
    caminho_imagem = request.POST.get('caminho_imagem')
    
    if caminho_imagem: 
        caminho_img ='dvds/img/' + caminho_imagem
    else:
        caminho_img = 'dvds/img/default.png'
    dvd = DVD(
        titulo = titulo,
        sinopse = sinopse,
        quantidade = quantidade,
        caminho_imagem = caminho_img,
    )  
    
    dvd.save()
    id = dvd.id
    
    Dvd = get_object_or_404(DVD, pk=id)
    
    return render(request, 'cadastro.html', {'dvd': Dvd})

    
@has_permission_decorator('remover_dvd')
def remover_dvd(request):
    id_dvd = request.POST.get('id')
    DVD.objects.filter(id = id_dvd).update(quantidade = F('quantidade') - 1)
    dvd = get_object_or_404(DVD, pk=id_dvd)
    cliente = get_object_or_404(Users, username = request.user)
    Aluguel = aluguel (
        id_dvd = dvd,
        id_cliente = cliente,
        nome = '{}_{}'.format(cliente.first_name, dvd.titulo),
        data_aluguel = datetime.now(),
    )
    Aluguel.save()
    if dvd.quantidade < 0:
        DVD.objects.filter(id = id).delete
    return render(request, 'aluguel.html', {'dvd' : dvd})    

@has_permission_decorator('inserir_lista_espera', redirect_to_login= '/clientes/login-cliente')
def inserir_lista_espera(request):
    dvd = get_object_or_404(DVD, pk = request.POST.get('id'))
    if lista_espera.objects.filter(cliente = request.user, dvd = dvd):
        return HttpResponse('Voce já esta na lista de espera para {}'.format(dvd.titulo))
    lista = lista_espera(
        cliente = request.user,
        dvd = dvd,
    )
    lista.save()
    return HttpResponse('Seu nome ta na lista')

@has_permission_decorator('deletar_dvd')
def deletar_dvd(request):
    id = request.POST.get('id')
    Dvd = get_object_or_404(DVD, pk=id)
    dvd = DVD.objects.filter(id = id)
    dvd.delete()
    return render(request, 'delete.html', { 'dvd' : Dvd })


@has_permission_decorator('devolver_dvd', redirect_to_login= '/clientes/login-cliente')
def devolver_dvd(request):
    _aluguel = get_object_or_404(aluguel, id = request.POST.get('id'))
    Aluguel = get_object_or_404(aluguel, id = request.POST.get('id'))
    tempo_aluguel = datetime.now().minute - Aluguel.data_aluguel.minute
    valor_aluguel = tempo_aluguel * 3.5
    cliente = get_object_or_404(Users, username = request.user)
    Aluguel.valor_aluguel = valor_aluguel
    context = {
        'aluguel' : _aluguel,
        'cliente' : cliente, 
        'tempo_aluguel' : tempo_aluguel,
        'nome_dvd' : Aluguel.id_dvd.titulo,
        'valor_aluguel' : valor_aluguel,
    }
    DVD.objects.filter(pk = Aluguel.id_dvd.id).update(quantidade = F('quantidade') + 1)
    return render(request, 'pagamento.html', context)


@has_permission_decorator('efetivar_pagamento_dvd', redirect_to_login= '/clientes/login-cliente')
def efetivar_pagamento_dvd(request):
    Aluguel = aluguel.objects.filter(pk =request.POST.get('id'))
    Aluguel.update(aluguel_dvd_pago = True)
    asyncio.sleep(60)
    Aluguel.delete()
    return render(request, 'confirmacao_pagamento.html')
    
    
    

