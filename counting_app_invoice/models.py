from pyexpat import model
from django.db import models
from counting_app_customer.models import Customer
from counting_app_cloth.models import Cloth
from counting_app_user.models import CustomUser

# Create your models here.

class Invoice(models.Model):
    owner = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    discount = models.IntegerField(blank=True , null=True)
    description = models.TextField(max_length=150 , blank=True , null = True)
    final_registration = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner_id)

class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice , on_delete=models.CASCADE)
    cloth = models.ForeignKey(Cloth , on_delete=models.CASCADE)
    count = models.IntegerField()
    code = models.IntegerField()
    price = models.IntegerField(blank=True , null=True)

    def __str__(self):
        return str(self.cloth.code)

