from factory import Faker
from factory.django import DjangoModelFactory
from django.conf import settings


class UserFactory(DjangoModelFactory):

    email = Faker("email")

    is_superuser = False
    is_staff = False

    class Meta:
        model = settings.AUTH_USER_MODEL
