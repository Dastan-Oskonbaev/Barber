from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    image = models.ImageField(
        _('Image'),
        upload_to='cities',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
