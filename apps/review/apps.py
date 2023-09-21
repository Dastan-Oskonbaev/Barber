from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReviewConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.review'
    verbose_name = _('Review')
    verbose_name_plural = _('Reviews')

    def ready(self):
        import apps.review.signals
