from django.db import models
from counting_app_user.models import CustomUser

# Create your models here.

class Customer(models.Model):
    owner = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=300)
    phonenumber = models.IntegerField()

    def __str__(self):
        return str(self.name)
