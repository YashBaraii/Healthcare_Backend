from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    PatientListCreateView,
    PatientDetailView,
    DoctorListCreateView,
    DoctorDetailView,
    MappingListCreateView,
    PatientMappingsView,
    MappingDeleteView,
)

urlpatterns = [
    path("auth/register/", RegisterView.as_view(), name="auth_register"),
    path("auth/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("patients/", PatientListCreateView.as_view(), name="patient-list-create"),
    path("patients/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),
    path("doctors/", DoctorListCreateView.as_view(), name="doctor-list-create"),
    path("doctors/<int:pk>/", DoctorDetailView.as_view(), name="doctor-detail"),
    path("mappings/", MappingListCreateView.as_view(), name="mapping-list-create"),
    path(
        "mappings/<int:patient_id>/",
        PatientMappingsView.as_view(),
        name="mapping-by-patient",
    ),
    path(
        "mappings/delete/<int:pk>/", MappingDeleteView.as_view(), name="mapping-delete"
    ),
]
