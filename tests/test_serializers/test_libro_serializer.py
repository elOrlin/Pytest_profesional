# tests/test_serializers/test_libro_serializer.py
import pytest
from apps.libro.serializers import LibroSerializer
from tests.factories.libro_factory import LibroFactory


@pytest.mark.django_db
def test_libro_serializer_valid_data():
    libro = LibroFactory.build()
    serializer = LibroSerializer(data={
        "titulo": libro.titulo,
        'autor': libro.autor,
        'disponible': libro.disponible,
        'borrower': libro.borrower
        # agrega otros campos necesarios
    })
    assert serializer.is_valid(), serializer.errors
    data = serializer.validated_data
    assert data["titulo"] == libro.titulo
