from django.db import models
from counting_app_user.models import CustomUser

# Create your models here.

class SellerOrTailor(models.Model):
    owner = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phonenumber = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.name