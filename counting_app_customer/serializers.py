from attr import fields
from rest_framework import serializers
from .models import Customer

class CustomersSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'