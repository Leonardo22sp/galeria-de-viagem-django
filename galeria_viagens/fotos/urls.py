from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('foto/<int:foto_id>/', views.detalhe_foto, name='detalhe_foto'),
    
    path('buscar/', views.buscar, name='buscar'),
]