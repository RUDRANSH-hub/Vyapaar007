from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    phone=models.IntegerField(max_length=10,default="")
    zip=models.CharField(max_length=50,default="")
    
    
    
        