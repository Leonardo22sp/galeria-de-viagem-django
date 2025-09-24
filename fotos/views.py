from django.shortcuts import render, get_object_or_404, redirect
from .models import Foto, CONTINENTES, ESTILOS
from .forms import ContatoForm
import csv
from datetime import datetime
import os

def index(request):
    fotos = Foto.objects.filter(publicada=True).order_by('-data_viagem')
    foto_destaque = Foto.objects.filter(publicada=True, destaque=True).order_by('?').first()
    contexto = {
        'cards': fotos,
        'continentes_list': CONTINENTES,
        'estilos_list': ESTILOS,
        'foto_destaque': foto_destaque,
    }
    return render(request, 'fotos/index.html', contexto)
def filtrar_estilo(request, estilo_slug):
    estilo_info = dict(ESTILOS)
    estilo_nome = estilo_info.get(estilo_slug, "Desconhecido")
    fotos_publicadas = Foto.objects.filter(publicada=True, estilo=estilo_slug).order_by('-data_viagem')
    contexto = {
        'cards': fotos_publicadas,
        'estilos_list': ESTILOS,
        'estilo_selecionado': estilo_nome,
        'continentes_list': CONTINENTES,
    }
    return render(request, 'fotos/index.html', contexto)

def detalhe_foto(request, foto_id):
    foto = get_object_or_404(Foto, pk=foto_id)
    return render(request, 'fotos/detalhe_foto.html', {'foto': foto})

def buscar(request):
    fotos_publicadas = Foto.objects.filter(publicada=True).order_by('-data_viagem')
    query = request.GET.get('q')
    if query:
        resultados = fotos_publicadas.filter(titulo__icontains=query)
    else:
        resultados = fotos_publicadas
    contexto = {
        'cards': resultados,
        'query': query,
        'continentes_list': CONTINENTES,
    }
    return render(request, 'fotos/index.html', contexto)

def filtrar_continente(request, continente_slug):
    continente_info = dict(CONTINENTES)
    continente_nome = continente_info.get(continente_slug, "Desconhecido")
    fotos_publicadas = Foto.objects.filter(publicada=True, continente=continente_slug).order_by('-data_viagem')
    contexto = {
        'cards': fotos_publicadas,
        'continentes_list': CONTINENTES,
        'continente_selecionado': continente_nome,
    }
    return render(request, 'fotos/index.html', contexto)

def sobre_nos(request):
    return render(request, 'fotos/sobre_nos.html')

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            data_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file_path = 'mensagens.csv'
            file_exists = os.path.isfile(file_path)
            with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['data_envio', 'nome', 'email', 'mensagem']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
                writer.writerow({
                    'data_envio': data_envio,
                    'nome': nome,
                    'email': email,
                    'mensagem': mensagem
                })
            return redirect('contato_sucesso')
    else:
        form = ContatoForm()
    return render(request, 'fotos/contato.html', {'form': form})

def contato_sucesso(request):
    return render(request, 'fotos/contato_sucesso.html')