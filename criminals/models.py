from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class criminal(models.Model):
    profile_pic = models.ImageField(upload_to='images/profiles/')
    fname= models.CharField(max_length=50)
    lname= models.CharField(max_length=50)
    dob=models.DateField(null=True, blank=True)
    contact_no=models.IntegerField()
    email=models.EmailField(max_length = 254)
    sex=models.CharField(max_length=50)
    residence=models.CharField(max_length=50)
    # pin=models.IntegerField()
    # district=models.CharField(max_length=50)
    # country=models.CharField(max_length=50)
    martial_status=models.CharField(max_length=50)
    height=models.IntegerField()
    identification=models.CharField(max_length=20)
    language=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    created_on=models.DateField(auto_now_add=True)
    updated_on=models.DateField(auto_now=True)

    def __str__(self):
        return self.fname
    
    def getallcriminals():
        return criminal.objects.all()
    
    def getcriminal(id):
        return criminal.objects.get(id=id)
    

class crime(models.Model):
    name=models.CharField(max_length=300)
    criminal=models.ForeignKey(criminal, on_delete=models.CASCADE)
    commited_on = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class documents(models.Model):
    attachment=models.ImageField(upload_to='images/attachments/')
    criminal=models.ForeignKey(criminal, on_delete=models.CASCADE)

    def __str__(self):
        return self.criminal.fname

class webimage(models.Model):
    name=models.ImageField(upload_to='images/attachments/')
    

class webvideo(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    vidname = models.FileField(upload_to='videos/')
    uploaded_on = models.DateTimeField( default=timezone.now)
    updated_on=models.DateTimeField(auto_now=True)
     
    

# class User(AbstractUser):
#     is_interviewer=models.BooleanField(default=False)

# class interviewer(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
