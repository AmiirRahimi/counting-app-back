from django.db import models
from counting_app_customer.models import Customer

# Create your models here.

class Cheque(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    serial_number = models.IntegerField()
    fishing_id = models.IntegerField()
    name = models.CharField(max_length=150)
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()