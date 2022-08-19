from django.contrib import admin
from .models import Registro, Espacos, HorariosDisponiveis, DiasSemanaisDisponiveis, DiasDisponiveis

# Register your models here.
# admin.site.register(Dados)
admin.site.register(Registro)
admin.site.register(Espacos)
admin.site.register(DiasSemanaisDisponiveis)
admin.site.register(HorariosDisponiveis)
admin.site.register(DiasDisponiveis)
