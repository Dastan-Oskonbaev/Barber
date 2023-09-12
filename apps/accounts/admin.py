from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, Barber, Profession, District, Language


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'email',
    )
    list_display_links = (
        'username',
    )
    search_fields = (
        'username',
        'email',
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": (
            "email",
            "first_name",
            "last_name",
            )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    save_on_top = True


@admin.register(Barber)
class BarberAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'email',
    )
    list_display_links = (
        'username',
    )
    search_fields = (
        'username',
        'email',
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": (
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "profession",
            "experience",
            "about_me",
            "district",
            "work_time_from",
            "work_time_to",
            "work_type",
            "languages",
            "city",
            )}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    save_on_top = True


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
    )


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
    )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    list_display_links = (
        'name',
    )
    search_fields = (
        'id',
        'name',
    )
