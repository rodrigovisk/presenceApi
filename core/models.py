from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nomeCompleto = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    matricula = models.CharField(max_length=9)

    def __str__(self):
        return self.nome
    