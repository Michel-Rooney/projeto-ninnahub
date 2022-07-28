from django.db import models

class Dados(models.Model):
    nome = models.CharField(max_length=255)
    cpnj = models.IntegerField()

    def __str__(self):
        return self.nome


#  class Meta:
#      db_table = 'dados'