# tests/test_serializers/test_biblioteca_serializer.py
import pytest
from apps.biblioteca.serializers import BibliotecaSerializer
from tests.factories.biblioteca_factory import BibliotecaFactory


@pytest.mark.django_db
def test_biblioteca_serializer_valid_data():
    biblioteca = BibliotecaFactory.build()
    serializer = BibliotecaSerializer(data={
        "nombre": biblioteca.nombre,
        "direccion": biblioteca.direccion,
    })
    assert serializer.is_valid(), serializer.errors
    data = serializer.validated_data
    assert data["nombre"] == biblioteca.nombre
