from django.db import models
from criminals.models import *

class education(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    school = models.CharField(max_length=50)
    schoolFrom= models.DateField(null=True, blank=True)
    schoolTo= models.DateField(null=True, blank=True)
    college = models.CharField(max_length=50)
    collegeFrom= models.DateField(null=True, blank=True)
    collegeTo= models.DateField(null=True, blank=True)
    
class communication(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    landline = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
class spouse(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    married = models.BooleanField(default=0)
    spouseName = models.CharField(max_length=50)
    daughterof = models.CharField(max_length=50)
    occupation =models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class kids(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    kidName = models.CharField(max_length=50)
    occupation =models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    college = models.CharField(max_length=60)

class financialdetails(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    incomesource = models.CharField(max_length=100)
    monthlyexpenses = models.CharField(max_length=100)
    propertyy = models.CharField(max_length=100)
    
class mobility(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    vehicalName = models.CharField(max_length=100)
    vehicalType = models.CharField(max_length=50)
    registrationNo = models.CharField(max_length=50)
    
    
