from CHANGE_ME.utils.lambda_handlers import EventHandler


class PreDeployHandler(EventHandler):
    def on_delete(self, event):
        pass

    def on_update(self, event):
        self.run_migrations(event=event)
        self.create_default_admin_user()

    def on_create(self, event):
        self.run_migrations(event=event)
        self.create_default_admin_user()


main = PreDeployHandler()
