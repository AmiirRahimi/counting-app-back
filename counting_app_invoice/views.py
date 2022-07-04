from django.forms import models
from django.shortcuts import render
from django.template import context
from rest_framework.views import APIView , Response
from .models import Invoice
from .serializer import InvoiceDetailsSerializer , InvoiceSerializer
from rest_framework import status
from .models import Invoice , InvoiceDetails
from counting_app_cloth.models import Cloth

# Create your views here.

class AddItemForNotRegisterdInvoice(APIView):
    def post(self , request):
        data = request.data
        invoice = Invoice.objects.filter(owner_id = request.user.id , final_registration = False , customer_id = data['customer']).first()
        if invoice is None:
            invoice = Invoice.objects.create(owner_id = request.user.id ,customer_id = data['customer'] )
        cloth = Cloth.objects.get(id = data['cloth'])
        invoice.invoicedetails_set.create(cloth_id = data['cloth'] , count = data['count'] , price = data['price'] , code = cloth.code)
        return Response(status = status.HTTP_200_OK)

class GetNotRegisterdInvoice(APIView):
    def post(self , request):
        data = request.data
        not_registerd_invoice = Invoice.objects.filter(owner_id = request.user.id , final_registration = False , customer_id = data['customer']).first()
        details = InvoiceDetails.objects.filter(invoice_id = not_registerd_invoice.id)
        total_price = 0
        total_count = 0
        for i in range(len(details)):
            total = details[i].price * details[i].count
            total += total_price
        for i in range(len(details)):
            details[i].count += total_count
        serializer = InvoiceDetailsSerializer(details , many = True )
        return Response(serializer.data , status = status.HTTP_200_OK)

class GetTotals(APIView):
    def post(self , request):
        data = request.data
        not_registerd_invoice = Invoice.objects.filter(owner_id = request.user.id , final_registration = False , customer_id = data['customer']).first()
        details = InvoiceDetails.objects.filter(invoice_id = not_registerd_invoice.id)
        total_price = 0
        total_count = 0
        for i in range(len(details)):
            total = details[i].price * details[i].count
            total_price += total
        for i in range(len(details)):
            total_count += details[i].count
        return Response({'total_price' : total_price , 'total_count' : total_count} , status=status.HTTP_200_OK)

class SubmitInvoice(APIView):
    def post(self , request):
        data = request.data
        print(data)
        invoice = Invoice.objects.filter(owner_id = request.user.id , final_registration = False , customer_id = data['customer']).first()
        if invoice is not None:
            invoice.final_registration = True
            invoice.discount = data['discount']
            invoice.description = data['description']
            invoice.save()
            return Response(status = status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class GetInvoices(APIView):
    def post(self , request):
        data = request.data
        invoice = Invoice.objects.filter(owner_id = request.user.id , final_registration = True , customer_id = data['customer'])
        serializer = InvoiceSerializer(invoice , many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)

