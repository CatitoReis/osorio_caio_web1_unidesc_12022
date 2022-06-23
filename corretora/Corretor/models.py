from tokenize import Double
from django.db import models

class Corretor(models.Model):

 comissao = models.IntegerField(max_length=100)
 id_corretor = models.CharField(max_length=100)

def calcular_salario(): Double





def __str__(self):
	return self.id_corretor
