from django.apps import AppConfig


class PrubaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pruba'

    def ready(self):
        import pruba.signals
