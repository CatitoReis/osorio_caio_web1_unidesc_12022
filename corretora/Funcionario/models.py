from inspect import _void
from tokenize import Double
from django.db import models

class Funcionario(models.Model):

 cpf = models.CharField(max_length=100)
 rg = models.CharField(max_length=100)
 nome = models.CharField(max_length=100)
 sexo = models.CharField(max_length=100)
 dataNascimento = models.DateField(max_length=100)
 carteiraTrabalho = models.CharField(max_length=100)
 salario = models.IntegerField(max_length=100)
 pis = models.CharField(max_length=100)



def consultar_Imoveis(): Double

def manter_Anuncio(): _void

def manter_Cliente(): _void

def manter_Funcionario(): _void

def manter_agendamento(): _void

def gerar_relatorio(): _void

def calcular_salario(): _void


def __str__(self):
	return self.cpf
