from django import forms

from .models import Prescription


class PrescriptionForm(forms.ModelForm):

    class Meta:
        model = Prescription

        fields = [
            'patient',
            'doctor',
            'medicine_name',
            'dosage',
            'frequency',
            'duration',
            'instructions',
        ]

        widgets = {
            'instructions': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Enter special instructions...'
                }
            ),
        }