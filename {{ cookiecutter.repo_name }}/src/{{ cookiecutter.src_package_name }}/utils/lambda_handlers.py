from mixbag.custom_resources import CustomResourceEventHandler
from drft.manage import manage_factory


manage = manage_factory()


def migrate(*args):
    return manage("migrate", *args)


class EventHandler(CustomResourceEventHandler):
    @staticmethod
    def run_migrations(event):
        properties = event["ResourceProperties"]
        app_label = properties["app_label"]
        migration_name = properties["migration_name"]
        migrate(app_label, migration_name, "--noinput", "--plan")
        migrate(app_label, migration_name, "--noinput")
        manage("showmigrations", "--plan")

    @staticmethod
    def create_default_admin_user():
        manage("create_default_admin_user")
