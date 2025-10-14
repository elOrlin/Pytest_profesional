import pytest
from faker import Faker
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pytest_profesional.settings")
django.setup()


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope="session")
def fake():
    return Faker("es_ES")
