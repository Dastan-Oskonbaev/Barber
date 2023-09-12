from django.contrib import admin

from .models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )
