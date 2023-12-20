# import
from django.db import models
from django.contrib.auth.models import User # username & password (inbuilt)

# Django models
# User model (profile)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Built in user, When user deleted - UserProfile will also be deleted
    birthday = models.DateField()
    phone = models.IntegerField()
    name = models.CharField(max_length=100)

# Bike model (bike details)
class Bike(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to="images/"
    ) 
    price = models.DecimalField(max_digits=8, decimal_places=2)
    engine = models.CharField(max_length=20)
    torque = models.CharField(max_length=50)
    weight = models.CharField(max_length=20)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
 
 # Message model (send mail)  
class Message(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
