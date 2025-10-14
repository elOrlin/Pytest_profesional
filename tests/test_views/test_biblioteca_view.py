# tests/test_views/test_biblioteca_views.py
import pytest
from rest_framework.test import APIClient
from tests.factories.biblioteca_factory import BibliotecaFactory


@pytest.mark.django_db
def test_biblioteca_create_view():
    client = APIClient()
    biblioteca = BibliotecaFactory.build()
    response = client.post("/api/bibliotecas/", {
        "nombre": biblioteca.nombre,
        "direccion": biblioteca.direccion
    }, format="json")
    assert response.status_code == 201
    assert response.data["nombre"] == biblioteca.nombre
