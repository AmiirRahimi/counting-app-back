from pyexpat import model
from turtle import ondrag
from django.db import models
from counting_app_user.models import CustomUser
from counting_app_sellerortailor.models import SellerOrTailor

# Create your models here.
class Cloth(models.Model):
    owner = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    seller_or_tailor_name = models.ForeignKey(SellerOrTailor , on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    code = models.IntegerField()
    count = models.IntegerField()
    seller_or_tailor_price = models.IntegerField()

    def __str__(self):
        return str(self.code)