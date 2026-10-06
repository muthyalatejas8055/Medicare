from django.db import models


class Prescription(models.Model):

    patient = models.ForeignKey(
        'patient_management.Patient',
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )

    doctor = models.ForeignKey(
        'doctor_management.Doctor',
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )

    medicine_name = models.CharField(max_length=150)

    dosage = models.CharField(max_length=100)

    frequency = models.CharField(max_length=100)

    duration = models.CharField(max_length=100)

    instructions = models.TextField(blank=True)

    prescribed_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.patient_id} - {self.medicine_name}"