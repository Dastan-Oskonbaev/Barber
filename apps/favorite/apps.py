from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FavoriteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.favorite'
    verbose_name = _('Favorite')
    verbose_name_plural = _('Favorites')
