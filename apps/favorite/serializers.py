from rest_framework import serializers

from .models import Favorite, FavoriteItem
from apps.accounts.serializers import BarberSerializer


class FavoriteItemSerializer(serializers.ModelSerializer):
    barber = BarberSerializer(read_only=True)

    class Meta:
        model = FavoriteItem
        fields = (
            'id',
            'favorite',
            'barber',
        )


class FavoriteSerializer(serializers.ModelSerializer):
    favorite_item = FavoriteItemSerializer(many=True, read_only=True)

    class Meta:
        model = Favorite
        fields = (
            'id',
            'user',
            'favorite_item',
        )
