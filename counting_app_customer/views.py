import stat
from django.shortcuts import render
from rest_framework.views import APIView , Response
from rest_framework import status
from .models import Customer
from .serializers import CustomersSerilizer

# Create your views here.

class AddCustomer(APIView):
    def post(self , request):
        data = request.data
        Customer.objects.create(owner_id = request.user.id , name = data['name'] , phonenumber = data['phonenumber'] , address = data['address'])
        return Response(status=status.HTTP_200_OK)

class GetCustomers(APIView):
    def get(self , request):
        customers = Customer.objects.filter(owner_id = request.user.id)
        serializer = CustomersSerilizer(customers , many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class GetCustomersForNotRegistered(APIView):
    def post(self , request):
        customers = Customer.invoice_set.objects.filter(final_registration = False)
        serializer = CustomersSerilizer(customers , many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
