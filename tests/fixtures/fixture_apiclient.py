import pytest
from rest_framework.test import APIClient
from tests.fixtures.usuario_fixtures import common_user_creation


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_api_client(common_user_creation):
    client = APIClient()
    client.force_authenticate(user=common_user_creation)
    return client
