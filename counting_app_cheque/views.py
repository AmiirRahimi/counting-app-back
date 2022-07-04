from django import views
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Cheque

# Create your views here.

class AddCheque(APIView):
    def post(self , request):
        data = request.data
        Cheque.objects.create(customer_id = data['customer'] , serial_number = data['serial'] , fishing_id = data['fishing_id'] , name = data['name'])