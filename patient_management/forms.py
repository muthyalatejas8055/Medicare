from django import forms

from .models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient

        fields = [
            'patient_id',
            'date_of_birth',
            'gender',
            'phone',
            'address',
            'blood_group',
            'emergency_contact',
            'medical_report',
        ]

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'rows': 4
                }
            ),

            'medical_report': forms.ClearableFileInput(
                attrs={
                    'accept': '.pdf'
                }
            ),
        }

    def clean_patient_id(self):
        patient_id = self.cleaned_data['patient_id'].strip()

        if not patient_id:
            raise forms.ValidationError(
                'Patient ID is required.'
            )

        return patient_id

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()

        if not phone.isdigit():
            raise forms.ValidationError(
                'Phone number must contain only digits.'
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                'Phone number must contain exactly 10 digits.'
            )

        return phone

    def clean_emergency_contact(self):
        contact = self.cleaned_data['emergency_contact'].strip()

        if contact and not contact.isdigit():
            raise forms.ValidationError(
                'Emergency contact must contain only digits.'
            )

        if contact and len(contact) != 10:
            raise forms.ValidationError(
                'Emergency contact must contain exactly 10 digits.'
            )

        return contact

    def clean_medical_report(self):
        report = self.cleaned_data.get('medical_report')

        if report:
            if not report.name.lower().endswith('.pdf'):
                raise forms.ValidationError(
                    'Only PDF files are allowed.'
                )

            if report.size > 5 * 1024 * 1024:
                raise forms.ValidationError(
                    'PDF file size must be 5 MB or less.'
                )

        return report