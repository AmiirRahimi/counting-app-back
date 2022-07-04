from django.urls import path
from .views import AddCloth , ClothesList

urlpatterns = [
    path('add/' , AddCloth.as_view()),
    path('list/' , ClothesList.as_view())
]
