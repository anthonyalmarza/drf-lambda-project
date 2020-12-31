import os

import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command

pytestmark = [pytest.mark.django_db]


def test_creation():
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    call_command("create_default_admin_user")
    assert user_model.objects.count() == 1
    user = user_model.objects.first()
    assert user.email == os.environ["DEFAULT_ADMIN_EMAIL"]
    assert user.check_password(os.environ["DEFAULT_ADMIN_PASSWORD"])


def test_password_update(settings):
    user_model = get_user_model()
    call_command("create_default_admin_user")
    user = user_model.objects.first()
    new_password = "new_password"
    assert not user.check_password(new_password)
    settings.DEFAULT_ADMIN_PASSWORD = new_password
    call_command("create_default_admin_user")
    user = user_model.objects.first()
    assert user.check_password(new_password)

    settings.DEFAULT_ADMIN_PASSWORD = None
    settings.DEFAULT_ADMIN_EMAIL = None
    call_command("create_default_admin_user")
