from django.contrib import admin

from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'doctor_id',
        'specialization',
        'qualification',
        'phone',
        'experience',
        'available',
    )

    search_fields = (
        'doctor_id',
        'specialization',
    )

    list_filter = (
        'specialization',
        'available',
    )