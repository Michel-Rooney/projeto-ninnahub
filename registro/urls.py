from unicodedata import name
from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('check/', views.check, name='check'),
    path('chamado/', views.abertura_chamado, name='abertura_chamado'),
    path('registro/', views.registro, name='registro'),
    path('<int:espaco_id>', views.descricao, name='descricao'),

    # path('gerenciar/', views.gerenciar, name='gerenciar'),
    # path('gerenciar/<int:espaco_id>', views.deletar, name='deletar'),

    path('gerenciar_espaco/', views.gerenciar_espaco, name='gerenciar_espaco'),
    path('adicionar_espaco/', views.adicionar_espaco, name='adicionar_espaco'),

    
    path('remover_espaco/', views.remover_espaco, name='remover_espaco'),
    path('remover_espaco/<int:espaco_id>', views.remover_espaco, name='remover_espaco'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)