import pytest
from tests.factories.usuario_factory import UsuarioFactory


@pytest.mark.django_db
def test_user_creation():
    usuario = UsuarioFactory()
    assert usuario.id is not None
    assert "@" in usuario.email
    assert hasattr(usuario, "telefono")