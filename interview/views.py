from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .filters import userfilter
from criminals.models import criminal

def subadmin(request):
    if request.user.is_authenticated:
        user=request.user
        que=questionAnswer.objects.filter(user=user)
        search = userfilter(request.GET, queryset=criminal.objects.all())
        searchdata = search.qs
    
        return render(request,'subadmin.html',{'que':que,'search':search, 'searchdata':searchdata})
    else:
        return redirect('userlogin')

def viewquestions(request,id):
    p=criminal.getcriminal(id)
    que=questionAnswer.objects.filter(criminal=id)
    print(que)
    return render(request,'questions.html',{'que':que})
