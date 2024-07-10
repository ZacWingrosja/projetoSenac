from django.contrib import admin
from jogos.models import Jogo

# Register your models here.
class ListandoJogo(admin.ModelAdmin):
    list_display = ("id", "nome", "plataforma")
    list_display_links = ("nome",)
    list_filter = ("nome",)

# Register your models here.
admin.site.register(Jogo, ListandoJogo)