from django.db import models

# Create your models here.
class myUser(models.Model):

    firstname = models.CharField(max_length=20,blank=False)
    lastname = models.CharField(max_length=20,blank=False)
    email = User.email
    password = User.password
