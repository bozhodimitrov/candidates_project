from django.apps import AppConfig


class CandidatesAppConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'candidates_app'

    def ready(self):
        import candidates_app.signals  # noqa: F401
