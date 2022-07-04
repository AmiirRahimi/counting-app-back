from attr import fields
from rest_framework import serializers
from .models import SellerOrTailor

class SellerOrTailorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerOrTailor
        fields = '__all__'