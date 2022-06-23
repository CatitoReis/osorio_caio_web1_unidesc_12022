from django.db import models

class Login(models.Model):

 email = models.CharField(max_length=100)
 senha = models.CharField(max_length=100)
 permissao = models.CharField(max_length=100)

def __str__(self):
	return self.email
