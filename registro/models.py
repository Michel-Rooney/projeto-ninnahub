from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import datetime

# class Dados(models.Model):
#     nome = models.CharField(max_length=255)
#     cpnj = models.IntegerField()

#     def __str__(self):
#         return self.nome,self.cnpj

class Registro(models.Model):
    #DADOS DA RESERVA
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
    #DADOS DO AGENTE E DA EMPRESA
    agente = models.CharField(max_length=30)
    mantenedor = models.CharField(max_length=30, choices=MANTENEDOR_CHOICES)
    empresa = models.CharField(max_length=30) 
    email = models.EmailField(max_length=254) 
    telefone = models.CharField(max_length=30)
    cpf = models.CharField(max_length=30)
    cnpj =models.CharField(max_length=30)
    descricao = models.TextField(max_length=1000)

    #DADOS DO EVENTO
    #ESPAÇO
    espacos = models.CharField(max_length=30, choices=EVENTO_CHOICES)
    #DATAS E HORA DO EVENTO
    data_reserva = models.DateField('Data da Reserva')
    hora_inicio = models.TimeField('Hora Início', default=datetime.time(0, 00), blank=True)
    hora_fim = models.TimeField('Hora Fim', default=datetime.time(0, 00))

    #DATAS E HORA DE CHECK IN/OUT
    check_in = models.BooleanField(default=False)
    check_in_horario = models.TimeField()
    check_out = models.BooleanField(default=False)
    check_out_horario = models.TimeField()

    #NUMERO DE PARTICIPANTES PRESENTES NO EVENTO
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


class NivelUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3
    )


class DiasSemanaisDisponiveis(models.Model):
    DIAS_SEMANAIS_CHOICES = (
        ('Seg', 'Segunda'),
        ('Ter', 'Terça'),
        ('Qua', 'Quarta'),
        ('Qui', 'Quinta'),
        ('Sex', 'Sexta'),
    )
    dia_semanal = models.CharField(max_length=3, choices=DIAS_SEMANAIS_CHOICES)

    def __str__(self):
        return self.dia_semanal

class HorariosDisponiveis(models.Model):
    HORARIOS_CHOICES = (
        ('09', '09:00'),
        ('10', '10:00'),
        ('11', '11:00'),
        ('12', '12:00'),
        ('13', '13:00'),
        ('14', '14:00'),
        ('15', '15:00'),
        ('16', '16:00'),
    )
    horarios = models.CharField(max_length=2, choices=HORARIOS_CHOICES)

    def __str__(self):
        return self.horarios


class DiasDisponiveis(models.Model):
    DIAS_CHOICES = (
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '18'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
    )
    dia = models.CharField(max_length=2, choices=DIAS_CHOICES)

    def __str__(self):
        return self.dia
