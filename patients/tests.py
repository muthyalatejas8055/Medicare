from datetime import date

from django.test import TestCase
from patient_management.models import Patient


class PatientModelTest(TestCase):

    def test_create_patient(self):
        patient = Patient.objects.create(
            patient_id="P001",
            date_of_birth=date(2000, 1, 1),
            gender="male",
            phone="9876543210",
            address="Hyderabad"
        )

        self.assertEqual(patient.patient_id, "P001")
        self.assertEqual(patient.gender, "male")