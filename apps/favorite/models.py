from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import CustomUser, Barber


class Favorite(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
    )

    def __str__(self):
        return f"{self.user}'s favorite"

    class Meta:
        verbose_name = _('Favorite')
        verbose_name_plural = _('Favorites')


class FavoriteItem(models.Model):
    favorite = models.ForeignKey(
        Favorite,
        on_delete=models.CASCADE,
        verbose_name=_('Favorite'),
        related_name='favorite_item',
    )
    barber = models.ForeignKey(
        Barber,
        on_delete=models.CASCADE,
        verbose_name=_('Barber'),
    )

    def __str__(self):
        return f"{self.barber} in {self.favorite.user}'s favorites"

    class Meta:
        verbose_name = _('Favorite item')
        verbose_name_plural = _('Favorite items')
