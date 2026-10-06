from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdminConfig(UserAdmin):

    list_display = (
        'email',
        'username',
        'role',
        'is_staff',
        'is_active',
    )

    search_fields = (
        'email',
        'username',
    )

    ordering = (
        'email',
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            'MediCare Plus Role',
            {
                'fields': (
                    'role',
                )
            }
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'MediCare Plus Role',
            {
                'fields': (
                    'role',
                )
            }
        ),
    )