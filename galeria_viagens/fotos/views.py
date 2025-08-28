from django.shortcuts import render, get_object_or_404
from .models import Foto

def index(request):
    """Renderiza a página inicial com todas as fotos publicadas."""
    fotos = Foto.objects.filter(publicada=True).order_by('-data_viagem')
    return render(request, 'fotos/index.html', {'cards': fotos})

def detalhe_foto(request, foto_id):
    """Renderiza a página de detalhes para uma única foto."""
    foto = get_object_or_404(Foto, pk=foto_id)
    return render(request, 'fotos/detalhe_foto.html', {'foto': foto})

def buscar(request):
    """Filtra as fotos com base em uma consulta de busca e reutiliza o template da página inicial para exibir os resultados."""
    fotos_publicadas = Foto.objects.filter(publicada=True).order_by('-data_viagem')
    
    query = request.GET.get('q')
    if query:
        resultados = fotos_publicadas.filter(titulo__icontains=query)
    else:
        resultados = fotos_publicadas

    contexto = {
        'cards': resultados,
        'query': query,
    }
    return render(request, 'fotos/index.html', contexto)