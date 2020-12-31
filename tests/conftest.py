import pytest
from rest_framework.test import APIClient

from factories.users import UserFactory


@pytest.fixture()
def user_password():
    return "password"


@pytest.fixture()
def user_email():
    return "test@test.com"


def _create_user(*, user_options: dict = None):
    user_options = user_options or {}
    user = UserFactory(**user_options)
    api_client = APIClient()
    api_client.force_authenticate(user=user)
    return user, api_client


@pytest.fixture()
def user_factory():
    return _create_user


@pytest.fixture()
def user(user_password, user_email):
    user = UserFactory(username=user_email, email=user_email)
    user.set_password(user_password)
    user.save(update_fields=["password"])
    return user


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def authed_client(user, api_client):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture()
def admin_client():
    user = UserFactory(is_superuser=True, is_staff=True)
    client = APIClient()
    client.force_login(user)
    return client
