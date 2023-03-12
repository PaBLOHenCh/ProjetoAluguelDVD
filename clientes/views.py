from multiprocessing import context
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from usuarios.models import Users
from rolepermissions.decorators import has_permission_decorator
from django.urls import reverse
from django.contrib import auth
from dvds.models import aluguel



from dvds.models import DVD


def clientes (request):
    lista = DVD.objects.all()
    context = {
        'lista' : lista,
    }
    return render(request, 'clientes.html', context)

def cadastro_cliente(request):
    if request.method == 'GET':
        return render(request, 'cadastrar_cliente.html')
    elif request.method == 'POST':
        username = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        first_name = request.POST.get('primeiro_nome')
        last_name = request.POST.get('ultimo_nome')
        
        cliente = Users.objects.filter(email=email)
        
        if cliente.exists():
            return HttpResponse("esse cliente já existe")
        else:    
            cliente = Users.objects.create_user(
            username = username,
            email = email,
            password = password,
            first_name = first_name,
            last_name = last_name,
            perfil = "C",
            )           
            return HttpResponse('Cliente cadastrado com sucesso')
        
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('clientes'))
        return render(request, 'login.html')
    elif request.method == 'POST':
        login = request.POST.get('email')
        password = request.POST.get('senha')
        
        user = auth.authenticate(username=login, password=password)
        
        if not user:
            return HttpResponse('Usuario invalido')
        auth.login(request, user)
        return HttpResponse('Usuario logado com sucesso')
    
@has_permission_decorator('dvds_alugados', redirect_to_login= '/clientes/login-cliente')
def dvds_alugados(request):
    cliente = get_object_or_404(Users, username= request.user)
    alugueis = aluguel.objects.filter(id_cliente = cliente.id)
    dvds = []
    
    for _aluguel in alugueis:
        dvds.append( _aluguel.id_dvd)
        
    context = {
        'dvds' : dvds,
        'alugueis': alugueis,
    }
    return render(request, 'alugueis.html', context)


# def teste_email(request):
#     send_mail('Assunto', 'Esse é um email de teste', 'pablohenriquechaves2101@outlook.com', ['pablohenriquechaves2101@gmail.com'])
#     return HttpResponse('sucesso')