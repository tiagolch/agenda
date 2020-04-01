from django.contrib import admin
from core.models import Evento


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'data_evento', 'data_criacao']


