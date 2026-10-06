from django.conf import settings
from django.db import models


class Doctor(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    doctor_id = models.CharField(
        max_length=20,
        unique=True
    )

    specialization = models.CharField(
        max_length=100
    )

    qualification = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=15
    )

    experience = models.PositiveIntegerField(
        default=0
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    available = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.doctor_id
