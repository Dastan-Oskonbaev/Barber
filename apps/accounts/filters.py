from django_filters import FilterSet

from .models import Barber


class BarberFilter(FilterSet):
    class Meta:
        model = Barber
        fields = {
            'district': ['exact'],
            'experience': ['exact'],
            'work_type': ['exact'],
        }
