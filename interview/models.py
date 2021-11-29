from django.db import models
from django.contrib.auth.models import User
from criminals.models  import *




class questionAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    criminal= models.ForeignKey(criminal, on_delete=models.CASCADE)
    question= models.CharField(max_length=500)
    answer= models.CharField(max_length=500)
    createdon= models.DateTimeField(auto_now_add=True)
    updatedon= models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.question[:15]

