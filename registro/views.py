from datetime import  time,timedelta,datetime 
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


