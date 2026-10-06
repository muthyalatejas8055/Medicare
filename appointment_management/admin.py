from django.contrib import admin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'patient',
        'doctor',
        'appointment_date',
        'appointment_time',
        'status',
    )

    search_fields = (
        'patient__patient_id',
        'doctor__doctor_id',
    )

    list_filter = (
        'status',
        'appointment_date',
    )

    ordering = (
        'appointment_date',
        'appointment_time',
    )