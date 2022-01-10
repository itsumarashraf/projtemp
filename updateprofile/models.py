from django.db import models
from criminals.models import *

class education(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    school = models.CharField(max_length=50,null=False)
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
    
class father(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    occupation =models.CharField(max_length=200)
    age =models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=50)

class mother(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    do = models.CharField(max_length=50)
    occupation =models.CharField(max_length=200)
    age =models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=50)
    address= models.CharField(max_length=200)

class grandfather(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address =models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    
class grandmother(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    do = models.CharField(max_length=50)
    address =models.CharField(max_length=200)
    phone = models.CharField(max_length=50)


class maternalgrandfather(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address =models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    
class maternalgrandmother(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    do = models.CharField(max_length=50)
    address =models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    
class brother(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    occupation =models.CharField(max_length=200)
    age =models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=50)

class brotherspouse(models.Model):
    brother = models.ForeignKey(brother,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50)
    do = models.CharField(max_length=100)
    address =models.CharField(max_length=200)
    occupation =models.CharField(max_length=200)
    
class brotherkids(models.Model):
    brother = models.ForeignKey(brother,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    occupation =models.CharField(max_length=200, null=True)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50, null=True)
    school = models.CharField(max_length=100, null=True)
    college =models.CharField(max_length=200, null=True) 
    

# *************************sister**************************

class sister(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    occupation =models.CharField(max_length=200)
    age =models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=50)

class sisterspouse(models.Model):
    sister = models.ForeignKey(sister,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50)
    do = models.CharField(max_length=100)
    address =models.CharField(max_length=200)
    occupation =models.CharField(max_length=200)
    
class sisterkids(models.Model):
    sister = models.ForeignKey(sister,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    occupation =models.CharField(max_length=200, null=True)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50, null=True)
    school = models.CharField(max_length=100, null=True)
    college =models.CharField(max_length=200, null=True) 
    


# *************************uncle**************************

class uncle(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    occupation =models.CharField(max_length=200)
    age =models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=50)

class unclespouse(models.Model):
    uncle = models.ForeignKey(uncle,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50)
    do = models.CharField(max_length=100)
    address =models.CharField(max_length=200)
    occupation =models.CharField(max_length=200)
    
class unclekids(models.Model):
    uncle = models.ForeignKey(uncle,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    occupation =models.CharField(max_length=200, null=True)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50, null=True)
    school = models.CharField(max_length=100, null=True)
    college =models.CharField(max_length=200, null=True)  
    
# ****************************aunt*?*********************************

class aunt(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    occupation =models.CharField(max_length=200)
    age =models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=50)

class auntspouse(models.Model):
    aunt = models.ForeignKey(aunt,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50)
    do = models.CharField(max_length=100)
    address =models.CharField(max_length=200)
    occupation =models.CharField(max_length=200)
    
class auntkids(models.Model):
    aunt = models.ForeignKey(aunt,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    occupation =models.CharField(max_length=200, null=True)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50, null=True)
    school = models.CharField(max_length=100, null=True)
    college =models.CharField(max_length=200, null=True) 
 
    
# *************************maternal uncle**************************

class maternaluncle(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    occupation =models.CharField(max_length=200)
    age =models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=50)

class maternalunclespouse(models.Model):
    maternaluncle = models.ForeignKey(maternaluncle,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50)
    do = models.CharField(max_length=100)
    address =models.CharField(max_length=200)
    occupation =models.CharField(max_length=200)
    
class maternalunclekids(models.Model):
    maternaluncle = models.ForeignKey(maternaluncle,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    occupation =models.CharField(max_length=200, null=True)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50, null=True)
    school = models.CharField(max_length=100, null=True)
    college =models.CharField(max_length=200, null=True)  
    
    
# ****************************maternal aunt*?*********************************

class maternalaunt(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    occupation =models.CharField(max_length=200)
    age =models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=50)

class maternalauntspouse(models.Model):
    maternalaunt = models.ForeignKey(maternalaunt,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50)
    do = models.CharField(max_length=100)
    address =models.CharField(max_length=200)
    occupation =models.CharField(max_length=200)
    
class maternalauntkids(models.Model):
    maternalaunt = models.ForeignKey(maternalaunt,on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    occupation =models.CharField(max_length=200, null=True)
    age =models.CharField(max_length=60)
    phone = models.CharField(max_length=50, null=True)
    school = models.CharField(max_length=100, null=True)
    college =models.CharField(max_length=200, null=True) 
    


# *****************************Militancy details*******************************
class militancydetails(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    organization = models.CharField(max_length=50)
    rank= models.CharField(max_length=50)
    militancy = models.TextField()
    infiltration = models.TextField()
    areas = models.TextField()
    sympathizers = models.TextField()
    arrest = models.TextField()
    recoveries =models.TextField()
    associates =models.TextField()
    
class detentiondetails(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    history = models.TextField()
    detentionplace =  models.CharField(max_length=100)
    prision = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    
class interrogratoropnion(models.Model):
    criminal = models.ForeignKey(criminal, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    opnion = models.TextField()