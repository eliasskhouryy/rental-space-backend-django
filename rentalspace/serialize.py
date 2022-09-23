from dataclasses import field, fields
from rest_framework import serializers
from rentalspace.models import VansModel
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class VansSerializer(serializers.ModelSerializer):
    class Meta:
        model = VansModel
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)
        return user