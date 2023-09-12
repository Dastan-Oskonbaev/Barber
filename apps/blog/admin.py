from django.contrib import admin

from .models import Category, Blog, Description


class DescriptionInline(admin.TabularInline):
    model = Description
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
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


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'date',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'name',
        'category',
        'date',
    )
    list_filter = (
        'name',
        'category',
        'date',
    )
    inlines = [
        DescriptionInline,
    ]
