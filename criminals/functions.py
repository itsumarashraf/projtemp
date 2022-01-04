from .models import *
from .locationmodel import *

def getaddressdetails(zipp):
    try:
        z = zipcode.objects.get(name=zipp)
        data={
            'country':z.country.name,
            'state':z.state.name,
            'district':z.district.name,
            'town':z.town.name                
        }
    except:
        data={
            'country':"",
            'state':"",
            'district':"",
            'town':"" 
        }
    return data

def saveaddress(user,address):
    country=address.get('country')
    state=address.get('state')
    district=address.get('district')
    town=address.get('town')
    zipcode=address.get('zip')
    
    criminaladdress.objects.create(criminal=user,country=country,state=state,district=district,town=town,zipcode=zipcode)
    return True