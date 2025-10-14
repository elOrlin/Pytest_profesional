from rest_framework import serializers
from apps.biblioteca.models import Biblioteca
from apps.libro.serializers import LibroSerializer


class BibliotecaSerializer(serializers.ModelSerializer):
    libros = LibroSerializer(many=True, read_only=True)

    class Meta:
        model = Biblioteca
        fields = ["id", "nombre", "direccion", "libros"]

    def validate_nombre(self, value):
        if not value:
            raise serializers.ValidationError("El nombre de la biblioteca no puede estar vacío")
        return value

    def validate_direccion(self, value):
        if not value:
            raise serializers.ValidationError("La dirección es obligatoria")
        return value
        return value
