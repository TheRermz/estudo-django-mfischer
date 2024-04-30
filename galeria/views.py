from django.shortcuts import render


def index(request):
    return render(request, 'alura-space/index.html')

def imagem(request):
    return render (request, 'alura-space/imagem.html')
