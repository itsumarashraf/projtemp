from django.shortcuts import render,HttpResponse
from .models import *
from .filters import userfilter
from criminals.models import criminal

def subadmin(request):
    user=request.user
    print(user)
    if user.is_authenticated:
        que=questionAnswer.objects.filter(user=user)
    
    search = userfilter(request.GET, queryset=criminal.objects.all())
    searchdata = search.qs
   
    return render(request,'subadmin.html',{'que':que,'search':search, 'searchdata':searchdata})

def viewquestions(request,id):
    p=criminal.getcriminal(id)
    que=questionAnswer.objects.filter(criminal=id)
    print(que)
    return render(request,'questions.html',{'que':que})
