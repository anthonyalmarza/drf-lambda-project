# type: ignore
# noqa
from django.contrib.postgres.operations import (
    CreateExtension,
    BtreeGinExtension,
    BtreeGistExtension,
    TrigramExtension,
    HStoreExtension,
)
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        # 3rd party apps
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("auth", "0011_update_proxy_permissions"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("sessions", "0001_initial"),
        ("sites", "0003_set_site_domain_and_name"),
        # Project apps
        # ("accounts", "0001_initial"),
        # ("users", "0001_initial"),
    ]

    operations = [
        # NOTE: if you want to add new extensions then add a new migration
        CreateExtension("postgis"),
        BtreeGistExtension(),
        BtreeGinExtension(),
        TrigramExtension(),
        HStoreExtension(),
    ]
