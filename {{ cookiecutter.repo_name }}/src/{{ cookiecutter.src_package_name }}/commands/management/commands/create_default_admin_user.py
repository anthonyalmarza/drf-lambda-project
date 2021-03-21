#!/usr/local/bin/python
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel = get_user_model()

    def handle(self, *args, **options):
        email = settings.DEFAULT_ADMIN_EMAIL
        password = settings.DEFAULT_ADMIN_PASSWORD

        if not email or not password:
            return

        try:
            user = self.UserModel.objects.get(email=email)
            # update password if it has changed
            if not user.check_password(password):
                user.set_password(password)
                user.save(update_fields=["password"])
        except self.UserModel.DoesNotExist:
            self.UserModel.objects.create_superuser(
                username=email, email=email, password=password
            )
