from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class Experience(TextChoices):
    INTERN = "I", _("Intern")
    SIX = "S", _("Six month")
    ONE = "O", _("One year")
    THREE = "T", _("Three year")
    FIVE = "F", _("Five year")
    MASTER = "M", _("Master")


class WorkType(TextChoices):
    SALON = "S", _("Salon")
    PRIVATE = "P", _("Private master")
