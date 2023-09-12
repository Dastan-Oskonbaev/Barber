from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'contact',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
        'contact',
    )
    list_filter = (
        'name',
        'contact',
    )
