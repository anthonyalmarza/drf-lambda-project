import pytest

pytestmark = [pytest.mark.django_db]


def test_user_admin(admin_client):
    response = admin_client.get("/admin/auth/user/")
    assert response.status_code == 200
