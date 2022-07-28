from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('check/', views.check, name='check'),
    path('chamado/', views.abertura_chamado, name='abertura_chamado'),
    path('registro/', views.registro, name='registro'),
]