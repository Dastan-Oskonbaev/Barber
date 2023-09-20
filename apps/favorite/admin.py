from django.contrib import admin

from .models import Favorite, FavoriteItem


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
    )
    list_display_links = (
        'user',
    )
    search_fields = (
        'id',
        'user',
    )


@admin.register(FavoriteItem)
class FavoriteItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'favorite',
        'barber',
    )
    list_display_links = (
        'favorite',
    )
    search_fields = (
        'id',
        'favorite',
        'barber',
    )
