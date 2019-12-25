from rest_framework import serializers
from .models import Cliente

# Serializers define the API representation.
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['url', 'nome', 'endereco', 'idade']
