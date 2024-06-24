from django.shortcuts import render
from .models import Jogo
def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'jogos/index.html', {'jogos':jogos})
