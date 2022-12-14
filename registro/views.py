from .models import NivelUsuario
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import  time, timedelta, datetime
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from .models import Espacos, Registro
import os
from ninnahub.settings import BASE_DIR
from django.contrib.auth.decorators import login_required


def home(request):
    """PAGINA INICIAL"""
    espaco = Espacos.objects.order_by('nome').all()
    return render(request, 'home.html', {'espacos' : espaco})

def descricao(request, espaco_id):
    """PAGINA DE DESCRIÇÂO DOS ESPAÇO"""
    espaco = get_object_or_404(Espacos, pk=espaco_id)
    return render(request, 'descricao.html', {'espaco' : espaco})

@login_required(login_url='/login')
def check(request):
    """PAGINA DE ADMINISTRADOR"""
    usuario = request.user.id
    conteudo = {"casos": Registro.objects.order_by('check_in_horario').all(),
    'nivel': get_object_or_404(NivelUsuario, usuario=usuario)
    }
    return render(request, 'check.html',conteudo)

def check_in(request,id):
    """REALIZAR CHECK IN/OUT DAS RESERVAS"""
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

def abertura_chamado(request):
    """PAGINA DE ABERTURA DE CHAMADO"""
    return render(request, 'abertura_chamado.html')

def registro(request):
    """PAGINA DE RESERVA DE ESPAÇO"""
    return render(request, 'registro.html')



# Gerenciamento de espaços

@login_required(login_url='/login')
def gerenciar_espaco(request):
    """PAGINA DE GERENCIAMENTO DE ESPAÇOS"""
    return render(request, 'espacos/gerenciar_espaco.html')

@login_required(login_url='/login')
def remover_espaco(request):
    """PAGINA DE REMOÇÂO DE ESPAÇO"""
    conteudo = {'espacos': Espacos.objects.order_by('nome').all()}
    return render(request, 'espacos/remover_espaco.html', conteudo)

@login_required(login_url='/login')
def remover_espaco_id(request, espaco_id):
    """REMOVER ESPAÇO ESPECIFICO"""
    espaco = get_object_or_404(Espacos, pk=espaco_id)
    os.remove(os.path.join(BASE_DIR, espaco.imagem1.path))
    espaco.delete()
    return redirect('/remover_espaco')

@login_required(login_url='/login')
def editar_espaco(request):
    """PAGINA DE EDIÇÂO DOS ESPAÇOS"""
    espaco = Espacos.objects.all()
    return render(request, 'espacos/editar_espaco.html', {'espacos' : espaco})

@login_required(login_url='/login')
def editar_espaco_id(request, espaco_id):
    """EDITAR ESPAÇO ESPECIFICO"""
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
        return redirect('/editar_espaco')

    espaco = get_object_or_404(Espacos, pk=espaco_id)
    return render(request, 'espacos/editar_espaco_id.html', {'espaco' : espaco})

@login_required(login_url='/login')
def adicionar_espaco(request):
    """ADCICIONAR ESPAÇO ESPECIFICO"""
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


#LOGIN ADM

def login(request):
    """PAGINA DE LOGIN DO ADMINISTRADOR"""
    if request.method ==  'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        #SE O EMAIL FOR VALIDO E CONSTAR NO BANCO
        if User.objects.filter(email = email).exists():
            nome = User.objects.filter(email = email).values_list('username',flat=True).get()
            user = auth.authenticate(request, username = nome, password = senha)
            if user is not None:
                auth.login(request, user)
                return redirect('check')
    return render(request,'login.html')

@login_required(login_url='/login')
def registro_adm(request):
    """PAGINA DE REGISTRO DE NOVO ADMINISTRADOR"""
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
    """REALIZAÇÂO DE LOGOUT DO USUARIO"""
    auth.logout(request)
    return redirect('/login')