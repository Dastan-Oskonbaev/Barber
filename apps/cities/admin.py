from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import City


@admin.register(City)
class CityAdmin(TranslationAdmin):
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
