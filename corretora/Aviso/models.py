from inspect import _void
from tokenize import Double
from django.db import models

class Aviso(models.Model):

 matricula_avi = models.IntegerField(max_length=100)
 assunto_avi = models.CharField(max_length=100)
 data_avi = models.DateField(max_length=100)



def incluir_aviso(): _void

def consultar_aviso(): Double

def remover_aviso(): _void


def __str__(self):
	return self.matricula_avi
