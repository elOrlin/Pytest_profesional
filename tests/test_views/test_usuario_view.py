# tests/test_views/test_usuario_views.py
import pytest
from rest_framework.test import APIClient
from tests.factories.usuario_factory import UsuarioFactory


@pytest.mark.django_db
def test_usuario_create_view():
    client = APIClient()
    libro = UsuarioFactory.build()
    usuario_data = {
        "email": libro.email,
        "nombre": libro.nombre,
        # otros campos obligatorios
    }
    response = client.post("/api/usuarios/", usuario_data, format="json")
    assert response.status_code == 201
    assert response.data["email"] == usuario_data["email"]
