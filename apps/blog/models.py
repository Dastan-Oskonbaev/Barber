from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Blog(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_('Category'),
        related_name='blog',
    )
    date = models.DateField(
        _('Date'),
        auto_now_add=True,
    )
    name = models.CharField(
        _('Name'),
        max_length=255,
    )
    image = models.ImageField(
        _('Image'),
        upload_to='blog',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')


class Description(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=255,
    )
    description = models.TextField(
        _('Description'),
    )
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        verbose_name=_('Blog'),
        related_name='description',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Description')
        verbose_name_plural = _('Descriptions')
