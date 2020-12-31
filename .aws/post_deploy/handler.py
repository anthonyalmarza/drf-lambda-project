from CHANGE_ME.utils.lambda_handlers import EventHandler


class PostDeployHandler(EventHandler):
    def on_delete(self, event):
        pass

    def on_update(self, event):
        self.run_migrations(event=event)

    def on_create(self, event):
        self.run_migrations(event=event)


main = PostDeployHandler()
