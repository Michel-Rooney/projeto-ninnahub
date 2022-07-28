from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'abertura_chamado.html')
