# tests/test_serializers/test_usuario_serializer.py
import pytest
from apps.usuario.serializers import UsuarioSerializer
from tests.factories.usuario_factory import UsuarioFactory


@pytest.mark.django_db
def test_usuario_serializer_valid_data():
    usuario = UsuarioFactory.build()  # build() para no guardar en DB
    serializer = UsuarioSerializer(data={
        "email": usuario.email,
        "nombre": usuario.nombre,
        # agrega otros campos de tu modelo Usuario
    })
    assert serializer.is_valid(), serializer.errors
    data = serializer.validated_data
    assert data["email"] == usuario.email
    assert data["nombre"] == usuario.nombre
