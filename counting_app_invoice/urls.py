from django.urls import path
from .views import AddItemForNotRegisterdInvoice , GetNotRegisterdInvoice , SubmitInvoice , GetTotals , GetInvoices

urlpatterns = [
    path('add/' , AddItemForNotRegisterdInvoice.as_view()),
    path('get-not-registerd/' , GetNotRegisterdInvoice.as_view()),
    path('submit/' , SubmitInvoice.as_view()),
    path('get_totals/' , GetTotals.as_view()),
    path('list/' , GetInvoices.as_view()),
]
