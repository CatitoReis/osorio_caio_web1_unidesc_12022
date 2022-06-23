from django.db import models


class Boleto(models.Model):

 codCliente = models.CharField(max_length=100)
 nomeCliente = models.CharField(max_length=100)




def __str__(self):
	return self.codCliente