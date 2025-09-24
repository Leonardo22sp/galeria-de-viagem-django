# fotos/admin.py
from django.contrib import admin
from .models import Foto

class FotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'local', 'data_viagem', 'publicada')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo', 'local', 'descricao')
    list_filter = ('local', 'data_viagem')
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Foto, FotoAdmin)