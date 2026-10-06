from django.contrib import admin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'patient_id',
        'gender',
        'phone',
        'blood_group',
        'created_at',
    )

    search_fields = (
        'patient_id',
        'phone',
    )

    list_filter = (
        'gender',
        'blood_group',
    )