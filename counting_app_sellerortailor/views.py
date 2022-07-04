from django.shortcuts import render
from rest_framework.views import APIView , Response
from .models import SellerOrTailor
from rest_framework import status
from .serializers import SellerOrTailorSerializer

# Create your views here.

class AddSellerOrTailor(APIView):
    def post(self , request):
        data = request.data
        SellerOrTailor.objects.create(owner_id = request.user.id , name = data['name'] , phonenumber = data['phonenumber'] , address = data['address'])
        return Response(status = status.HTTP_200_OK)

class GetSellerOrTailor(APIView):
    def get(self , request):
        seller_or_tailor = SellerOrTailor.objects.filter(owner_id = request.user.id)
        serializer = SellerOrTailorSerializer(seller_or_tailor , many = True)
        return Response(serializer.data , status = status.HTTP_200_OK)