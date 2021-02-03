import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Customer(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,verbose_name="email address", unique=True)
    id_number = models.IntegerField()
    contact_info = models.IntegerField()
    display_pic = models.ImageField(upload_to="profiles", default="user.jpg")
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'id_number', 'contact_info']

    class Meta:
        verbose_name_plural = "Customers"
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
