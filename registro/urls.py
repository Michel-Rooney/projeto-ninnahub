from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('check/', views.check, name='check'),
    path('chamado/', views.abertura_chamado, name='abertura_chamado'),
    path('registro/', views.registro, name='registro'),
    path('<int:espaco_id>', views.descricao, name='descricao')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)