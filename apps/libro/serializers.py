from rest_framework import serializers
from .models import Libro


class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'disponible', 'borrower']

    def validate_isbn(self, value):
        if len(value) not in [10, 13]:
            raise serializers.ValidationError("El ISBN debe tener 10 o 13 caracteres.")
        return value

    def validate_titulo(self, value):
        if not value:
            raise serializers.ValidationError("El título no puede estar vacío.")
        return value
