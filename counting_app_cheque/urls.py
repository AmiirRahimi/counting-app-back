from django.urls import path
from .views import AddCheque

urlpatterns = [
    path('add' , AddCheque.as_view())
]
