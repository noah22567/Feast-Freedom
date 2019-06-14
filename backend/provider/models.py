from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ServiceProvider(models.Model):
    userID = models.ForeignKey(myUser,on_delete=models.CASCADE)
    ServiceProviderName = models.CharField(max_length=20)


class Kitchen(ServiceProvider, models.Model):

    ServiceProviderID = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    Starttime = models.TimeField(auto_now=False,blank=False)
    Endtime = models.TimeField(auto_now=False,blank=False)
    Kitchenimg = models.ImageField(upload_to="images/",blank=True)

class MenuItem(models.Model):

    kitchenID = models.ForeignKey(Kitchen,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20, blank=False)
    Veg = models.BooleanField(null=True)
    Price = models.DecimalField(max_digits=10000, decimal_places=2)

