from inspect import _void
from tokenize import Double
from django.db import models

class Agendamento(models.Model):

 dia = models.DateField(max_length=100)
 hora = models.DateField(max_length=100)
 local = models.CharField(max_length=100)





def incluir_agendamento(): _void

def consultar_agendamento(): Double

def alterar_agendamento(): _void

def remover_agendamento(): _void


def __str__(self):
	return self.dia