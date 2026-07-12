from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Fields",
            {
                "fields": (
                    "role",
                    "created_at",
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "email",
                    "role",
                )
            },
        ),
    )

    readonly_fields = ("created_at",)