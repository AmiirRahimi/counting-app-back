from requests_toolbelt import user_agent
from rest_framework.views import APIView , Response
from django.contrib.auth import authenticate , login
from rest_framework import status
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.permissions import AllowAny , IsAuthenticated

# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class CheckPhonenumber(TokenViewBase):
    permission_classes = [AllowAny]
    def post(self , request):
        phonenumber = request.data['phonenumber']
        try:
            user = CustomUser.objects.get(phonenumber = phonenumber)
        except:
            return Response(status = status.HTTP_204_NO_CONTENT)
        else:
            if user is not None:
                return Response(status = status.HTTP_200_OK)


class Login(TokenViewBase):
    permission_classes = [AllowAny]
    def post(self , request):
        phonenumber = request.data['phonenumber']
        password = request.data['password']
        user = authenticate(phonenumber = phonenumber , password = password)
        if user is not None:
            login(request , user)
            return Response(get_tokens_for_user(user),status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

class GetUserData(APIView):
    permission_classes = [IsAuthenticated]
    def post(self , request):
        UserData = {
            'full_name' : request.user.first_name + request.user.last_name,
            'phonenumber' : request.user.phonenumber
        }
        return Response(UserData , status = status.HTTP_200_OK)
        