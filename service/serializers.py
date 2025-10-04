from rest_framework import serializers
from . import models


# convert the service model data into JSON
class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = "__all__"
