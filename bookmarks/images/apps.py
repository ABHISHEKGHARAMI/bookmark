from django.apps import AppConfig


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'
    
    
    # importing the signal for when its populated
    def ready(self):
        import images.signals
