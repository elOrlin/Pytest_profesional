from rest_framework import serializers
from apps.usuario.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["id", "nombre", "email", "fecha_publicacion", "activo", "apellido",  "telefono"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Debe ser un email válido")
        return value

    def create(self, validated_data):
        # Podrías hashear la contraseña aquí si quieres
        return Usuario.objects.create(**validated_data)
