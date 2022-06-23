from django.db import models

class Pessoa(models.Model):

 matricula = models.IntegerField(max_length=100)
 telefone = models.CharField(max_length=100)
 CEP = models.CharField(max_length=100)
 rua = models.CharField(max_length=100)
 bairro = models.CharField(max_length=100)
 cidade = models.CharField(max_length=100)
 uf = models.CharField(max_length=100)
 


def __str__(self):
	return self.matricula