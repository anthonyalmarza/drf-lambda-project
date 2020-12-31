import pytest

pytestmark = [pytest.mark.django_db]


def test_sites_0003_rollback(migrator, settings):
    old_state = migrator.apply_initial_migration(
        ("sites", "0003_set_site_domain_and_name")
    )
    site = old_state.apps.get_model("sites", "Site")
    assert site.objects.get(id=settings.SITE_ID).domain == settings.SITE_DOMAIN

    migrator.apply_tested_migration(("sites", "0002_alter_domain_unique"))
    assert site.objects.get(id=settings.SITE_ID).domain == "example.com"
