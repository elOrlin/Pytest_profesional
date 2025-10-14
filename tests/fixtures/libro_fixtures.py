from typing import Generator
import pytest
from apps.libro.models import Libro
from tests.factories.libro_factory import LibroFactory


@pytest.fixture
def libro_creation() -> Generator[Libro, None, None]:
    libro = LibroFactory()
    yield libro
