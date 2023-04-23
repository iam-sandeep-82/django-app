from django.apps import AppConfig


class App1Config(AppConfig):
    name = 'App_1'
    def ready(self):
        import App_1.signals
