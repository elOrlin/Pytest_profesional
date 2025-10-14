from unittest.mock import Mock


def mock_service():
    service = Mock()
    service.process.return_value = True
    return service
