from django.db import models

# Create your models here.CLS

class Register(models.Model):
    fullname=models.CharField(max_length=50)
    email=models.CharField(primary_key=True,max_length=50)
    password=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    desig=models.CharField(max_length=50,default="user")     #whenever we created a new column,compulsary we have to give default value
def __str__(self):
    return self.mail+" 2"+ self.fullname