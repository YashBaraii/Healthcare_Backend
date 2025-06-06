from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    # Fix reverse accessor clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="api_user_groups",  # Custom reverse name
        blank=True,
        help_text="The groups this user belongs to.",
        related_query_name="api_user",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="api_user_permissions",  # Custom reverse name
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="api_user",
    )

    def __str__(self):
        return self.email


class Patient(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="doctor_mappings"
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="patient_mappings"
    )

    class Meta:
        unique_together = ("patient", "doctor")

    def __str__(self):
        return f"{self.patient.name} ↔ {self.doctor.name}"
