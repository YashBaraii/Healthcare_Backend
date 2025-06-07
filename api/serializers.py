from rest_framework import serializers
from .models import User, Patient, Doctor, PatientDoctorMapping
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ["created_by"]


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source="patient.name", read_only=True)
    doctor_name = serializers.CharField(source="doctor.name", read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ["id", "patient", "patient_name", "doctor", "doctor_name"]

    def validate(self, data):
        patient = data.get("patient")
        doctor = data.get("doctor")

        if not Patient.objects.filter(id=patient.id).exists():
            raise ValidationError({"patient": "Patient does not exist."})
        if not Doctor.objects.filter(id=doctor.id).exists():
            raise ValidationError({"doctor": "Doctor does not exist."})
        if PatientDoctorMapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise ValidationError("This doctor is already assigned to this patient.")
        return data
