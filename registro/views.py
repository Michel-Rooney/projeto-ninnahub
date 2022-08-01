from datetime import  time,timedelta,datetime 
from django.shortcuts import get_object_or_404, render, HttpResponse
from .models import Dados, Espacos, Registro

def home(request):
    espaco = Espacos.objects.all()

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


        
