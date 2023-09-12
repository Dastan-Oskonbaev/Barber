from rest_framework import serializers

from .models import City
from apps.accounts.serializers import BarberSerializer


class CitySerializer(serializers.ModelSerializer):
    barber = BarberSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = (
            'id',
            'name',
            'image',
            'barber',
        )
