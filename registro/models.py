from email.policy import default
from django.db import models

class Dados(models.Model):
    nome = models.CharField(max_length=255)
    cpnj = models.IntegerField()

    def __str__(self):
        return self.nome


#  class Meta:
#      db_table = 'dados'


class Registro(models.Model):
    MANTENEDOR_CHOICES = (
        ('Mantenedor', 'Mantenedor'), 
        ('Residente Startup', 'Residente Startup'), 
        ('Time Operacional', 'Time Operacional'),
    )

    EVENTO_CHOICES = (
        ('Espaço01', 'Espaço01'),
        ('Espaço02', 'Espaço02'),
        ('Espaço03', 'Espaço03'),
    )


    agente = models.CharField(max_length=30)
    mantenedor = models.CharField(max_length=30, choices=MANTENEDOR_CHOICES)
    empresa = models.CharField(max_length=30)
    evento = models.CharField(max_length=30, choices=EVENTO_CHOICES) 
    email = models.EmailField(max_length=254) 
    telefone = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
    cnpj =models.CharField(max_length=30)
    descricao = models.TextField(max_length=1000)
    
    check_in = models.BooleanField(default=False)
    check_in_horario = models.TimeField()
    check_out = models.BooleanField(default=False)
    check_out_horario = models.TimeField()
    participantes_presentes = models.IntegerField(default=0)

    def __str__(self):
        return self.agente


class Espacos(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.TextField(max_length=1000)

    imagem1 = models.ImageField(upload_to='fotos/espacos/imagem1', blank=True)
    imagem2 = models.ImageField(upload_to='fotos/espacos/imagem2', blank=True)
    imagem3 = models.ImageField(upload_to='fotos/espacos/imagem3', blank=True)
    imagem4 = models.ImageField(upload_to='fotos/espacos/imagem4', blank=True)

    def __str__(self):
        return self.nome