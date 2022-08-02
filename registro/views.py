from datetime import  time,timedelta,datetime 
<<<<<<< HEAD
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
=======
>>>>>>> 15d5b585fd715701aa08e7c363801b8b405d0b7c
from .models import Dados, Espacos, Registro
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
import os
from ninnahub.settings import BASE_DIR

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


# def check(request,id=None):
#     if request.method == 'POST':
#         quantidade = request.POST['quantidade']
#         check_out= Registro.objects.get(id=id)
#         check_out.participantes_presentes = quantidade
#         check_out.check_out_horario = datetime.now().strftime('%H:%M:%S')
#         check_out.save()
#     conteudo = {"casos": Registro.objects.order_by('check_in_horario').all()}
#     return render(request, 'check.html',conteudo)


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





def gerenciar_espaco(request):
    return render(request, 'espacos/gerenciar_espaco.html')

def adicionar_espaco(request):
    return render(request, 'espacos/adicionar_espaco.html')

def remover_espaco(request, espaco_id=None):
    if request.method == 'POST':
        try:
            deletar = request.POST['deletar']
        except:
            return redirect('/remover_espaco')
        
        if deletar:
            espaco = Espacos.objects.order_by('nome').get(id=espaco_id)
            os.remove(os.path.join(BASE_DIR, espaco.imagem1.path))
            espaco.delete()
            return redirect('/remover_espaco')


    espaco = Espacos.objects.all()
    espacos_a_exibir = {
        'espacos' : espaco
    }

    return render(request, 'espacos/remover_espaco.html', espacos_a_exibir)


