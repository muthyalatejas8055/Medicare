from django import forms
from django.utils import timezone

from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment

        fields = [
            'patient',
            'doctor',
            'appointment_date',
            'appointment_time',
            'reason',
            'status',
        ]

        widgets = {
            'appointment_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'appointment_time': forms.TimeInput(
                attrs={
                    'type': 'time'
                }
            ),

            'reason': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Enter reason for appointment...'
                }
            ),
        }

    def clean_appointment_date(self):
        appointment_date = self.cleaned_data['appointment_date']

        if appointment_date < timezone.localdate():
            raise forms.ValidationError(
                'Appointment date cannot be in the past.'
            )

        return appointment_date