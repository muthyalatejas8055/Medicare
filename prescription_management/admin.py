from django.contrib import admin

from .models import Prescription


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):

    list_display = (
        'patient',
        'doctor',
        'medicine_name',
        'dosage',
        'frequency',
        'duration',
        'prescribed_date',
    )

    search_fields = (
        'patient__patient_id',
        'doctor__doctor_id',
        'medicine_name',
    )

    list_filter = (
        'prescribed_date',
    )