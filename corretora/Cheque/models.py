from django.db import models

class Cheque(models.Model):

 financeira = models.CharField(max_length=100)
 nomeCliente = models.CharField(max_length=100)
 numero = models.CharField(max_length=100)
 dataAbertura = models.DateField(max_length=100)



def __str__(self):
	return self.financeira