from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    # custom query with built in function for patient
    def get_queryset(self):
        queryset = super().get_queryset()  # parent(L-8) has been inherited here
        patient_id = self.request.query_params.get(
            "patient_id"
        )  # getting the patient id
        if patient_id:
            queryset = queryset.filter(
                patient_id=patient_id
            )  # patient id exits: then show details
        return queryset  # or show all (the parent)

    # custom query with built in function for doctor
    def get_queryset(self):
        queryset = super().get_queryset()  # parent(L-8) has been inherited here
        doctor_id = self.request.query_params.get("doctor_id")  # getting the patient id
        if doctor_id:
            queryset = queryset.filter(
                doctor_id=doctor_id
            )  # patient id exits: then show details
        return queryset  # or show all (the parent)
