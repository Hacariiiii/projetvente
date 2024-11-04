from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class user(models.Model) :
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    username=models.CharField(max_length=200,null=True, blank=True )
    email=models.CharField(max_length=200,null=True, blank=True )
    password=models.CharField(max_length=200, null=True , blank=True )
    repassword=models.CharField(max_length=200 , null=True , blank=True )
    name=models.CharField(max_length=200 , null=True , blank=True )
    price=models.IntegerField( null=True , blank=True )

class product(models.Model) :
 
    name=models.CharField(max_length=200,null=True ,blank=True )
    price=models.CharField(max_length=200,null=True, blank=True )
    description=models.CharField(max_length=200,null=True, blank=True )
    image=models.ImageField(null=True, blank=True)
   
   
    


    

