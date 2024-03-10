from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

class Dog(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dog_name = models.CharField(max_length=50)
    breed = models.CharField(max_length=50)
    age = models.IntegerField()

class Service(models.Model):
    service_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    notes = models.TextField()
