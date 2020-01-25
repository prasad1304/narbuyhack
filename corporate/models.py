from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

import uuid 


class Items(models.Model):
    item_name = models.CharField(max_length=50)
    item_quantity = models.FloatField()
    price = models.FloatField()
    product_description = models.CharField(max_length=150)
    image=models.ImageField(upload_to='farmers')
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    shop=models.ForeignKey('ContactModel', on_delete=models.CASCADE)
    def __str__(self):
        return str(self.item_name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:


            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Corporate(models.Model):
    access_user = models.ForeignKey(
        'ContactModel', on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class ContactModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=100,unique=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    
    area= models.CharField(max_length=100)
    password = models.CharField(max_length=20, unique=True)
    verify = models.BooleanField(default=False)
    email = models.CharField(max_length=100)

 

    def __str__(self):

        return self.shop_name


class CorperateGroup(models.Model):
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE)
    shop = models.ForeignKey(ContactModel, on_delete=models.CASCADE)
    image = models.ImageField(default='download.jpg', upload_to='groups')
    
   
    user = models.ManyToManyField(Items, blank=True, null=True)
   
    price = models.FloatField(default=0, blank=True)
  

    def __str__(self):
        return self.shop.shop_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:


            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
