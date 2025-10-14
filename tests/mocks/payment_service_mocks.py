from unittest.mock import MagicMock


def mock_payment_service():
    mock = MagicMock()
    mock.charge.return_value = {"status": "success", "id": "12345"}
    return mock
