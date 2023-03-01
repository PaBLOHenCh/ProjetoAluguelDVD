from django.shortcuts import render, get_object_or_404
from .models import DVD
from django.http import HttpResponse
from django.db.models import F


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

def remover_dvd(request):
    id = request.POST.get('id')
    DVD.objects.filter(id = id).update(quantidade = F('quantidade') - 1)
    dvd = get_object_or_404(DVD, pk=id)
    if dvd.quantidade == 0:
        Dvd = DVD.objects.filter(id = id)
        Dvd.delete()
    return render(request, 'aluguel.html', {'dvd' : dvd})

def deletar_dvd(request):
    id = request.POST.get('id')
    Dvd = get_object_or_404(DVD, pk=id)
    dvd = DVD.objects.filter(id = id)
    dvd.delete()
    return render(request, 'delete.html', { 'dvd' : Dvd })