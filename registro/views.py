from django.shortcuts import render, HttpResponse
from .models import Dados

def home(request):
    return render(request, 'home.html')

def check(request):
    conteuto = {"casos": Dados.objects.all()}
    return render(request, 'check.html',conteuto)

def abertura_chamado(request):
    return render(request, 'abertura_chamado.html')

def registro(request):
    return render(request, 'registro.html')
