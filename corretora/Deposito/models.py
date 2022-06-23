from django.db import models

class Deposito(models.Model):

	idDeposito = models.CharField(max_length=100)


def __str__(self):
	return self.idDeposito