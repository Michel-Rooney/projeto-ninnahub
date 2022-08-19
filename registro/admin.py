from django.contrib import admin
from .models import Registro, Espacos, HorariosDisponiveis, DiasDisponiveis

# Register your models here.
# admin.site.register(Dados)
admin.site.register(Registro)
admin.site.register(Espacos)
admin.site.register(DiasDisponiveis)
admin.site.register(HorariosDisponiveis)
