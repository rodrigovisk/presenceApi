from rest_framework import serializers
from .models import Pessoa

# Serializers define the API representation.
class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['url', 'nomeCompleto', 'cpf', 'matricula']