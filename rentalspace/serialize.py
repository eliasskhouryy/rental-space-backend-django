from dataclasses import field, fields
from rest_framework import serializers
from rentalspace.models import VansModel

class VansSerializer(serializers.ModelSerializer):
    class Meta:
        model = VansModel
        fields = "__all__"