from django.shortcuts import render,HttpResponse,redirect
from .models import *
from .filters import *
from criminals.models import *
from criminals.urls import *
from django.http import HttpResponseRedirect

def subadmin(request):
    if request.user.is_authenticated:
        user=request.user
        que=questionAnswer.objects.filter(user=user)
        search = userfilter(request.GET, queryset=criminal.objects.filter(deleted=False))
        searchdata = search.qs
    
        return render(request,'subadmin.html',{'que':que,'search':search, 'criminal':searchdata})
    else:
        return redirect('userlogin')

def viewquestions(request,id):
    p=criminal.getcriminal(id)
    que=questionAnswer.objects.filter(criminal=id)
    if request.method=='POST':
        if request.POST.get('question'):
            questionAnswer.objects.create(user=request.user,criminal=p,question=request.POST['question'],answer=request.POST['answer'])
        else:
            review.objects.create(user=request.user, criminal=p, review=request.POST['review'])
    return render(request,'questions.html',{'que':que})

def profile(request,id):
    cri=criminal.objects.get(id=id)
    if request.POST.get('review'):
        review.objects.create(user=request.user, criminal=cri, review=request.POST['review'])
    return render(request,'criminalprofile.html',{'criminal':cri})

def deletequeans(request,id):
    questionAnswer.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def reviews(request,id):
    r=review.objects.filter(criminal__id=id)
    return render(request,'reviews.html',{'reviews':r})