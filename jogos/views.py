from django.shortcuts import render, get_object_or_404
from jogos.models import Jogo
# Create your views here.
def index(request):
    jogos = Jogo.objects.all()
    return render(request, 'jogos/index.html', {"cards":jogos})