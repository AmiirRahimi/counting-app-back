from rest_framework.urls import path
from .views import CheckPhonenumber , Login , GetUserData

urlpatterns = [
    path('check-phonenumber/' , CheckPhonenumber.as_view()),
    path('login/' , Login.as_view()),
    path('get-user-data/' , GetUserData.as_view()),
]
