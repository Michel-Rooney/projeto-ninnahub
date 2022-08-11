from .models import NivelUsuario
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import  time,timedelta,datetime
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Dados, Espacos, Registro
import os
from ninnahub.settings import BASE_DIR
from django.contrib.auth.decorators import login_required


def home(request):
    espaco = Espacos.objects.order_by('nome').all()

    espacos_a_exibir = {
        'espacos' : espaco
    }

    return render(request, 'home.html', espacos_a_exibir)

def descricao(request, espaco_id):
    espaco = get_object_or_404(Espacos, pk=espaco_id)

    espacos_a_exibir = {
        'espaco' : espaco
    }

    return render(request, 'descricao.html', espacos_a_exibir)

def check_in(request,id):
    checando = get_object_or_404(Registro,pk=id)
    if checando.check_in == False:
        checando.check_in = True
        checando.check_in_horario = datetime.now().strftime('%H:%M:%S')
    else:
        checando.check_in =False
        quantidade = request.POST['quantidade']
        checando.participantes_presentes = quantidade
        checando.check_out_horario = datetime.now().strftime('%H:%M:%S')
    checando.save()
    return redirect('check')


def check(request):
    conteudo = {"casos": Registro.objects.order_by('check_in_horario').all()}
    return render(request, 'check.html',conteudo)

def abertura_chamado(request):
    return render(request, 'abertura_chamado.html')

def registro(request):
    return render(request, 'registro.html')


# Gerenciamento de espaços

def gerenciar_espaco(request):
    return render(request, 'espacos/gerenciar_espaco.html')


def remover_espaco(request):
    conteudo = {'espacos': Espacos.objects.order_by('nome').all()}
    return render(request, 'espacos/remover_espaco.html', conteudo)

def remover_espaco_id(request, espaco_id):
    if request.method == 'POST':
        try:
            deletar = request.POST['deletar']
        except:
            return redirect('/remover_espaco')
        
        if deletar:
            espaco = get_object_or_404(Espacos, pk=espaco_id)
            os.remove(os.path.join(BASE_DIR, espaco.imagem1.path))
            espaco.delete()
            return redirect('/remover_espaco')


    espaco = Espacos.objects.all()
    espacos_a_exibir = {
        'espacos' : espaco
    }

    return render(request, 'espacos/remover_espaco.html', espacos_a_exibir)


def editar_espaco(request):
    espaco = Espacos.objects.all()
    espacos_a_exibir = {
        'espacos' : espaco
    }

    return render(request, 'espacos/editar_espaco.html', espacos_a_exibir)

def editar_espaco_id(request, espaco_id):
    if request.method == 'POST':
        espaco = Espacos.objects.get(id=espaco_id)
        
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        imagem1 = request.FILES['imagem1']
        # imagem2 = request.FILES['imagem2']
        # imagem3 = request.FILES['imagem3']
        # imagem4 = request.FILES['imagem4']

        try:
            os.remove(os.path.join(BASE_DIR, espaco.imagem1.path))
        except:
            pass

        espaco.nome = nome
        espaco.descricao = descricao
        espaco.imagem1 = imagem1
        espaco.save()


    espaco = get_object_or_404(Espacos, pk=espaco_id)

    espaco_a_exibir = {
        'espaco' : espaco
    }
    return render(request, 'espacos/editar_espaco_id.html', espaco_a_exibir)


def adicionar_espaco(request):
    if request.method == 'POST':

        nome = request.POST['nome']
        descricao = request.POST['descricao']
        imagem1 = request.FILES['imagem1']
        # imagem2 = request.FILES['imagem2']
        # imagem3 = request.FILES['imagem3']
        # imagem4 = request.FILES['imagem4']

        try:
            os.remove(os.path.join(BASE_DIR, espaco.imagem1.path))
        except:
            pass
        
        espaco = Espacos.objects.create(nome=nome, descricao=descricao, imagem1=imagem1)
    
    return render(request, 'espacos/adicionar_espaco.html')





#login adm

def login(request):
    if request.method ==  'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if User.objects.filter(email = email).exists():
            nome = User.objects.filter(email = email).values_list('username',flat=True).get()
            user = auth.authenticate(request, username = nome, password = senha)
            if user is not None:
                auth.login(request, user)
                return redirect('check')
    return render(request,'login.html')

@login_required(login_url='/login')
def registro_adm(request):
    if request.method == 'POST':
        nome = request.POST['nome_usuario']
        email = request.POST['email']
        senha = request.POST['senha']
        tipo = request.POST['nivel']
        user =User.objects.create_user(username = nome, email = email,  password = senha)
        user.save()
        user_id = User.objects.get(email = email)
        user_n = get_object_or_404(User, pk= user_id.id)
        nivel = NivelUsuario.objects.create(usuario = user_n, status= tipo)
        nivel.save()
        return redirect('login')
    return render(request, 'registro_adm.html')

def logout(request):
    auth.logout(request)
    return redirect('/login')