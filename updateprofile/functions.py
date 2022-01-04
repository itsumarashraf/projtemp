from .models import *
from criminals.models import criminal



def seteducation(id,data):
    criminalid = criminal.getcriminal(id)
    education.objects.create(criminal =criminalid,school=data['school'],college=data['collage'],schoolFrom=data['schoolfrom'],
                             schoolTo=data['schoolto'], collegeFrom=data['collagefrom'],collegeTo=data['collageto']
                             )
    
def setcommunications(id,data):
    criminalid = criminal.getcriminal(id)
    communication.objects.create(criminal=criminalid,phone=data['phone'],landline=data['landline'],email=data['email'])

def setmarriagedetails(id,data):
    criminalid = criminal.getcriminal(id)
    if data['married']=='no':
        pass
    else:
        spouse.objects.create(criminal=criminalid,married= 1,spouseName=data['spousename'],daughterof=data['spousefather'],occupation=data['spouseoccupaion'],
                              address=data['spouseaddress'],age=data['spouseage'],phone=data['spousephone'])
        
        kidnames = data.getlist('kidname')
        occ = data.getlist('kidoccupation')
        age = data.getlist('kidage')
        phone = data.getlist('kidphone')
        school = data.getlist('kidschool')
        collage = data.getlist('kidcollage')
        
        for n,o,a,p,s,c in zip(kidnames,occ,age,phone,school,collage):
            kids.objects.create(criminal=criminalid, kidName=n, occupation=o,age=a,phone=p,school=s,college=c)
            
def setfinancialdetails(id,data):
    criminalid = criminal.getcriminal(id)
    financialdetails.objects.create(criminal=criminalid,incomesource=data['incomesourse'],monthlyexpenses=data['monthlyincome'],propertyy=data['property'])

def setmobilitydetails(id,data):
    pass
        
        
        