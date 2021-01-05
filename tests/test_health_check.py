import pytest
from rest_framework import status


pytestmark = [pytest.mark.django_db]


def test_health_check(api_client):
    response = api_client.get("/health-check/")
    assert response.status_code == status.HTTP_200_OK
