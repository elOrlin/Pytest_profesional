from typing import Generator
import pytest
from apps.biblioteca.models import Biblioteca
from tests.factories.biblioteca_factory import BibliotecaFactory


@pytest.fixture
def biblioteca_creation() -> Generator[Biblioteca, None, None]:
    biblioteca = BibliotecaFactory()
    yield biblioteca
