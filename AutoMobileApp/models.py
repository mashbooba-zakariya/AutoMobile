from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#---------Model for Login--------
class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)


#---------Model for Customer Register---------
class Customer(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    mobile = models.CharField(max_length=50)
    vehicle_No = models.CharField(max_length=50)
    Aadhar_No = models.CharField(max_length=16)


#---------Model for Manager Register---------
class Manager(models.Model):

    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    ManagerId = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    mobile = models.CharField(max_length=50)
    Aadhar_No = models.CharField(max_length=16)


#-------------Scheduling Booking slot from admin----------------
class Schedules(models.Model):

    date = models.DateField()
    Start_time = models.TimeField()
    end_time = models.TimeField()


# ------------Booking from Customer-------------
class Appointment(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    Slots = models.ForeignKey(Schedules, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)


#----------feedback from customer------------

class Feedback(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    description = models.TextField()
    reply = models.TextField(null=True,blank=True)