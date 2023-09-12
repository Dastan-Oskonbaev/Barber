from django.db import models
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField

from .constants import Experience, WorkType


class CustomUser(AbstractUser):
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')


class Profession(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('Profession')
        verbose_name_plural = _('Professions')


class District(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('District')
        verbose_name_plural = _('Districts')


class Language(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255,
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')


class Barber(AbstractUser):
    profession = models.ForeignKey(
        Profession,
        on_delete=models.DO_NOTHING,
        verbose_name=_('Profession'),
        null=True,
        blank=True,
    )
    experience = models.CharField(
        _('Experience'),
        max_length=1,
        choices=Experience.choices,
        default=Experience.INTERN,
    )
    about_me = models.TextField(
        _('About me'),
        null=True,
        blank=True,
    )
    district = models.ForeignKey(
        District,
        on_delete=models.DO_NOTHING,
        verbose_name=_('District'),
        null=True,
        blank=True,
    )
    phone_number = PhoneNumberField(
        _('Phone number'),
        null=True,
        blank=True,
    )
    work_time_from = models.TimeField(
        _('Work time from'),
        default='10:00',
    )
    work_time_to = models.TimeField(
        _('Work time to'),
        default='22:00',
    )
    work_type = models.CharField(
        _('Work type'),
        max_length=1,
        choices=WorkType.choices,
        default=WorkType.PRIVATE,
    )
    languages = models.ManyToManyField(
        Language,
        verbose_name=_('Languages'),
    )
    address = models.CharField(
        _('Address'),
        max_length=255,
        null=True,
        blank=True,
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="barber_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="barber_set",
        related_query_name="user",
    )

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name = _('Barber')
        verbose_name_plural = _('Barbers')
