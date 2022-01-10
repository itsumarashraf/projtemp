from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
import uuid

class criminalcategory(models.Model):
    categoryname = models.CharField(max_length=50)
    
    def __str__(self):
        return self.categoryname
    
class criminal(models.Model):
    category = models.ForeignKey(criminalcategory, on_delete=models.SET_NULL, null=True)
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    code= models.CharField(max_length=100, default = uuid.uuid4().hex[:6].upper())
    dob=models.DateField(null=True, blank=True)
    gender=models.CharField(max_length=50)
    martial_status=models.CharField(max_length=50)
    pending=models.BooleanField(default=1)
    deleted=models.BooleanField(default=0)
    interviewed =models.BooleanField(default=0)
    imprisioned = models.BooleanField(default=1)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)
    tags = TaggableManager()

    def __str__(self):
        return self.fname
    
    def getallcriminals():
        return criminal.objects.all()
    
    def getcriminal(id):
        return criminal.objects.get(id=id)
    
    def addtags(user,tags):
        for tag in tags.split(","):
            user.tags.add(tag)
    
class criminalImages(models.Model):
    criminal=models.ForeignKey(criminal, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/profiles/')
    

class criminalvideo(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    vidname = models.FileField(upload_to='videos/')
    uploaded_on = models.DateTimeField( default=timezone.now)
    updated_on=models.DateTimeField(auto_now=True)
    

class criminaladdress(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    town=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=50)
    
    def __str__(self):
        return self.district
     
class crime(models.Model):
    crimname=models.CharField(max_length=300)
    criminal=models.ForeignKey(criminal, on_delete=models.CASCADE)
    commited_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


def get_upload_path(instance, filename):
    return 'images/attachments/'

class documents(models.Model):
    documentname= models.CharField(max_length=50)
    attachment=models.FileField(upload_to='images/attachments/')
    criminal=models.ForeignKey(criminal, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.criminal.fname

    



     
    
