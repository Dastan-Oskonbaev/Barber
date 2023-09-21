from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import Category, Blog, Description


class DescriptionInline(TranslationTabularInline):
    model = Description
    extra = 1


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
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
class BlogAdmin(TranslationAdmin):
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
