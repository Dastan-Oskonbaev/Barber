from rest_framework import serializers

from .models import Favorite, FavoriteItem


class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    favorite_item = FavoriteItemSerializer(many=True, read_only=True)

    class Meta:
        model = Favorite
        fields = (
            'id',
            'user',
            'favorite_item',
        )
