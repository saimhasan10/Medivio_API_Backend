from rest_framework import serializers
from . import models


# doctor serializer
class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    specialization = serializers.StringRelatedField(many=True)
    designation = serializers.StringRelatedField(many=True)
    available_time = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Doctor
        fields = "__all__"


# specialization serializer
class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = "__all__"


# designation serializer
class DesignationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Designation
        fields = "__all__"


# available time serializer
class AvailableTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AvailableTime
        fields = "__all__"


# Review serializer
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Review
        fields = "__all__"
