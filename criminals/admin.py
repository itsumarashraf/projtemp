from django.contrib import admin
from .locationmodel import *
# Register your models here.
from criminals.models import *
from criminals.locationmodel import *
admin.site.register(crime)
admin.site.register(criminal)
admin.site.register(documents)
admin.site.register(criminalImages)
admin.site.register(criminalvideo)
admin.site.register(criminaladdress)
admin.site.register(country)
admin.site.register(states)
admin.site.register(district)
admin.site.register(town)
admin.site.register(zipcode)
