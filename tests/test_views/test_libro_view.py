# tests/test_views/test_libro_views.py
import pytest
from rest_framework.test import APIClient
from tests.factories.libro_factory import LibroFactory


@pytest.mark.django_db
def test_libro_create_view():
    client = APIClient()
    libro = LibroFactory.build()
    response = client.post("/api/libros/", {
        "titulo": libro.titulo,
        'autor': libro.autor,
        'disponible': libro.disponible,
        'borrower': libro.borrower
    }, format="json")
    assert response.status_code == 201
    assert response.data["titulo"] == libro.titulo
