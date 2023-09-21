from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CitiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cities'
    verbose_name = _('City')
    verbose_name_plural = _('Cities')
