from CHANGE_ME.utils.lambda_handlers import EventHandler


handler = EventHandler()


def test_event_handler_admin_user(mocker):
    manage = mocker.patch("CHANGE_ME.utils.lambda_handlers.manage")
    handler.create_default_admin_user()
    assert manage.called
    assert manage.called_once_with("create_default_admin_user")


def test_event_handler_migrations(mocker):
    manage = mocker.patch("CHANGE_ME.utils.lambda_handlers.manage")
    handler.run_migrations(
        {"ResourceProperties": {"app_label": "test", "migration_name": "0001"}}
    )
    assert manage.called
    assert manage.called_with("migrate", "test", "0001")
