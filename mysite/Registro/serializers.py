from .models import Cliente
from rest_framework import serializers


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'telefono',
                  'direccion', 'email', 'contraseña']

