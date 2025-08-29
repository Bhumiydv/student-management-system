from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30,null=True)
    email=models.CharField(max_length=30,null=True)
    phone=models.CharField(max_length=10,null=True)
    college=models.CharField(max_length=30,null=True)
    city=models.CharField(max_length=30,null=True)
    jdate=models.CharField(max_length=30,null=True)
    tfee=models.CharField(max_length=20,null=True)
    pfee=models.CharField(max_length=20,null=True)
    lfee=models.CharField(max_length=30,null=True)
    technology=models.CharField(max_length=30,null=True)
    image=models.FileField(null=True)

class contactus(models.Model):
    full_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    description = models.CharField(max_length=200,null=True)