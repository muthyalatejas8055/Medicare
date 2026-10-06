from django import forms

from .models import Doctor


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor

        fields = [
            'doctor_id',
            'specialization',
            'qualification',
            'phone',
            'experience',
            'consultation_fee',
            'available',
        ]

        widgets = {
            'experience': forms.NumberInput(
                attrs={
                    'min': 0
                }
            ),

            'consultation_fee': forms.NumberInput(
                attrs={
                    'step': '0.01',
                    'min': 0
                }
            ),
        }