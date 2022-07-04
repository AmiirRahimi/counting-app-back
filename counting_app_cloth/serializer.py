from attr import fields
from rest_framework import serializers
from .models import Cloth

class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        fields = '__all__'