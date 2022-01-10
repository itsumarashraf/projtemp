from django.shortcuts import render
from .functions import *
from django.db import transaction


# @adminOnly
@transaction.atomic
def updateprofile(request,id):
    if request.method == "POST":
        data = request.POST
        seteducation(id,data)
        # setcommunications(id,data)
        # setmarriagedetails(id,data)
        # setfinancialdetails(id,data)
        # setmobilitydetails(id,data)
        
        # setparentdetails(id,data)
        # setgrandparentdetails(id,data)
        # setbrotherdetails(id,data)
        # setsisterdetails(id,data)
        # setpaternaluncledetails(id,data)
        # setpaternalauntdetails(id,data)
        # setmaternaluncledetails(id,data)
        # setmaternalauntdetails(id,data)
        
        # setmilitancydetails(id,data)
        # setdetentiondetails(id,data)
        # setinterrogatordetails(id,data)
        # print(data)
    return render(request,'updateprofile.html')