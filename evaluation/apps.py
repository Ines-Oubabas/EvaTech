from django.apps import AppConfig


class EvaluationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'evaluation'

def ready(self):
        import evaluation.signals  # Import des signaux