from django.shortcuts import render
from jogos.models import Jogo
def lista_jogos(request):
    jogos = Jogo.objects.all()
    return render(request, 'jogos/index.html', {'cards':jogos})
