from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.models import CustomUser, Barber


class Review(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name=_('User'),
        related_name='review_user',
    )
    barber = models.ForeignKey(
        Barber,
        on_delete=models.CASCADE,
        verbose_name=_('Barber'),
        related_name='review_barber',
    )
    text = models.TextField(
        _('Text'),
    )
    rating = models.PositiveIntegerField(
        _('Rating'),
        choices=[
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        ],
        default=5,
    )
    date = models.DateField(
        _('Date'),
        auto_now_add=True,
    )

    def __str__(self):
        return f'Review by {self.user.username} on {self.barber.username}'

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
