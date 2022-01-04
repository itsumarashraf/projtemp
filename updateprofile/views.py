from django.shortcuts import render
from .functions import *
from django.db import transaction


# @adminOnly
@transaction.atomic
def updateprofile(request,id):
    if request.method == "POST":
        data = request.POST
        # seteducation(id,data)
        # setcommunications(id,data)
        # setmarriagedetails(id,data)
        # setfinancialdetails(id,data)
        # setmobilitydetails(id,data)
        print(data)
    return render(request,'updateprofile.html')