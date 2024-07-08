from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    lancamento = models.DateField()
    plataforma = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='imagens_jogos/', null=True, blank=True)

    def __str__(self):
        return self.nome