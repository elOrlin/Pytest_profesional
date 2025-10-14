from typing import Generator
import pytest
from apps.usuario.models import Usuario
from tests.factories.usuario_factory import UsuarioFactory

@pytest.fixture
def common_user_creation() -> Generator[Usuario, None, None]:
    user = UsuarioFactory()
    yield user
