from modeltranslation.translator import register, TranslationOptions

from .models import Category, Blog, Description


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(Description)
class DescriptionTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )
