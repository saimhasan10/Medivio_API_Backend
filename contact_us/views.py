from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers


class ContactUsViewset(viewsets.ModelViewSet):
    # this will convert to JSON
    queryset = models.ContactUs.objects.all()  # data come from the model
    serializer_class = serializers.ContactUsSerializer  # convert to serializers
