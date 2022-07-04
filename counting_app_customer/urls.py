from rest_framework.urls import path
from .views import AddCustomer , GetCustomers , GetCustomersForNotRegistered

urlpatterns = [
    path('add/' , AddCustomer.as_view()),
    path('list/' , GetCustomers.as_view()),
    path('list/for-not-registered' , GetCustomersForNotRegistered.as_view()),
]