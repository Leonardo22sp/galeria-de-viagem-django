from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('foto/<int:foto_id>/', views.detalhe_foto, name='detalhe_foto'),
    path('buscar/', views.buscar, name='buscar'),
    path('continente/<slug:continente_slug>/', views.filtrar_continente, name='filtrar_continente'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('contato/', views.contato, name='contato'),
    path('contato/sucesso/', views.contato_sucesso, name='contato_sucesso'),
]