from django.db import models
from django.conf import settings


# Create your models 
  

class Product(models.Model):
        CATEGORY =(
            ('Car','Car'),
            ('Scooter','Scooter'),
            ('Motorcycle','Motorcycle'),
            )

        name = models.CharField(max_length=40 , null =True)
        price = models.CharField(max_length=40, null =True)
        category = models.CharField(max_length=40 , null =True,choices = CATEGORY)
        description = models.CharField(max_length=40 , null =True,blank=True)
        date_created = models.DateTimeField(auto_now_add=True, null =True)

        def __str__(self):
            return self.category


class Booking(models.Model):
        user = models.CharField(max_length=40,null=True)
        Product = models.CharField(max_length=40,null=True)
        date =models.DateField(max_length=40,null=True)
        time = models.CharField(max_length=40,null=True)
        phone = models.CharField(max_length=40 , null=True)
             
        def __str__(self):
            return f'{self.user} has booked {self.Product}from {self.date} at {self.time}'


    

