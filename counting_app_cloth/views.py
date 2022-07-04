from django.shortcuts import render
from rest_framework.views import APIView , Response
from rest_framework import status
from .models import Cloth
from .serializer import ClothesSerializer
# Create your views here.

class AddCloth(APIView):
    def post(self , request):
        data = request.data
        print(data)
        Cloth.objects.create(owner_id = request.user.id , seller_or_tailor_name_id = data['sellerortailor'] , name = data['name'] , code = data['code'] , count = data['count'] , seller_or_tailor_price = data['v_price'])
        return Response(status=status.HTTP_200_OK)

class ClothesList(APIView):
    def get(self , request):
        clothes = Cloth.objects.filter(owner_id = request.user.id)
        serializer = ClothesSerializer(clothes , many = True)
        return Response(serializer.data , status = status.HTTP_200_OK)
    