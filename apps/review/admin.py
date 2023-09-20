from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'barber',
        'rating',
        'date',
    )
    list_display_links = (
        'user',
    )
    search_fields = (
        'id',
        'user',
        'barber',
        'rating',
        'date',
    )
    list_filter = (
        'id',
        'user',
        'barber',
        'rating',
        'date',
    )
