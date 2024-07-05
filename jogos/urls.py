from django.urls import path
from jogos.views import lista_jogos

urlpatterns = [
    path('', lista_jogos, name='index')
]
