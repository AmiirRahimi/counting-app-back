from rest_framework.urls import path
from .views import AddSellerOrTailor , GetSellerOrTailor

urlpatterns = [
    path('add/' , AddSellerOrTailor.as_view()),
    path('list/' , GetSellerOrTailor.as_view())
]
