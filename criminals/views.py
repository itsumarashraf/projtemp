from django.shortcuts import redirect,render,HttpResponse
from criminals import views
from .form import *
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models  import *
from criminals.locationmodel import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .decorators import *
import json
import base64
import io
from PIL import Image
from django.core.files.base import ContentFile
from .functions import *


@adminOnly
# @permission_required('criminals.delete_crime')
def home(request):
    count=criminal.objects.all().count()
    pending=criminal.objects.filter(pending=True).count()
    jailed=criminal.objects.filter(imprisioned=True).count()
    free=criminal.objects.filter(imprisioned=False).count()
    return render(request,'index.html',{'total':count,'pending':pending,'imprisioned':jailed,'free':free})

@adminOnly
def viewcriminals(request):
    criminals= criminal.objects.filter(deleted=False)
    return render(request,'viewcriminals.html',{'criminal':criminals})

@csrf_exempt
@adminOnly
def addcriminal(request):
    ccategroy = criminalcategory.objects.all()
    
    
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        gender=request.POST.get('gender')
        martialstatus=request.POST.get('martialstatus')
        dob=request.POST.get('dob')
        tag=request.POST.get('tag')
        address=request.POST
        cid=request.POST.get('ccategory')
        cc=criminalcategory.objects.get(id=cid)
        if request.FILES.getlist('img'):
            
            user= criminal(category=cc,fname=fname,lname=lname,dob=dob,martial_status=martialstatus,gender=gender)
            user.save()
            # saves address of user
            saveaddress(user,address)
            
            criminal.addtags(user,tag)
            for pic in request.FILES.getlist('img'):
                criminalImages.objects.create(criminal=user,image=pic)

                
        elif request.POST.get('webcam'):
            user= criminal(category=cc,fname=fname,lname=lname,dob=dob,martial_status=martialstatus,gender=gender)
            user.save()
            data=request.POST.get('webcam')
            imagecode=json.loads(data)
            for image in imagecode:
                format, imgstr = image.split(';base64,')
                ext = format.split('/')[-1]
                print('extension is  :',ext)
                data = ContentFile(base64.b64decode(imgstr), name='webcamimage.'+ ext)
                
                criminalImages.objects.create(criminal=user,image=data)
            
            # saves tags for a user
            criminal.addtags(user,tag)
            # saves addres of user
            saveaddress(user,address)
            
        else:
            if request.POST.get('zipp'):
                zipp=request.POST.get('zipp')
                data=getaddressdetails(zipp)
                return HttpResponse(json.dumps(data))
                    
        
    return render(request,'addcriminal.html',{'cc':ccategroy})


@adminOnly
def viewcriminal(request,id):
    cri=criminal.getcriminal(id)
    return render(request,'criminal.html',{'criminal':cri})


def uploaddocuments(request,id):
    if request.method=="POST":
        document = request.FILES.getlist('docs')
        cri=criminal.objects.get(id=id)
        for doc in document:
            documents.objects.create(criminal=cri,documentname=request.POST.get('docname'), attachment=doc)
        
    doc=documents.objects.filter(criminal__id=id)
    return render(request,'uploaddocs.html',{'document':doc})

@adminOnly
def addcrime(request,id):
    crim=criminal.objects.get(id=id)
    crime_form = CrimeForm(request.POST or None, instance =crim)
    if crime_form.is_valid():
        crime_form.save()
        return redirect('home')
    return render(request,'addcrime.html',{'form':crime_form})

@adminOnly
def editcriminal(request,id):
    person=criminal.objects.get(id=id)
    if request.method=='POST':
        print(request.POST)
    return render(request,'editcriminal.html',{'person':person})


def userlogin(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            uname=request.POST.get('uname')
            password=request.POST.get('password')
            user=authenticate(request,username=uname,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            
            msg='Incorrect Username or Password'
            return render(request,'userlogin.html',{'msg':msg})
            
        return render(request,'userlogin.html')
    else:
        return redirect('home')


def userlogout(request):
    logout(request)
    return redirect('userlogin')
    
@adminOnly
def register(request):
    form =UserCreationForm(request.POST)
    if form.is_valid():
        form.instance.is_staff=True
        form.save()
    return render(request,'register.html',{'form':form})


def criminalvid(request,id):
    vid =criminalvideo.objects.filter(criminal=id)
    cri=criminal.objects.get(id=id)
    if request.method=="POST":
        for video in request.FILES.getlist('videos'):
            criminalvideo.objects.create(criminal=cri,vidname=video)
    return render(request,'video.html',{'umar':vid})


@csrf_exempt
def recordvideo(request,id):
    crim=criminal.objects.get(id=id)
    if request.method=='POST':
        criminalvideo.objects.create(criminal=crim, vidname=request.FILES.get('file'))
    return render(request, 'recordvideo.html',{'criminal':crim})

def pendingcases(request):
    cri = criminal.objects.filter(pending=1)
    print(cri)
    return render(request,'pendingcases.html',{'criminal':cri})

def filterbytag(request,tslug):
    search = criminal.objects.filter(tags__slug=tslug)
    return render(request,'filterbytag.html',{'search':search})

def veiwtrashcriminals(request):
    criminals= criminal.objects.filter(deleted=True)
    return render(request,'trash.html',{'criminal':criminals})

def trashcriminal(request,id):
    search = criminal.objects.get(id=id)
    search.deleted=True
    search.save()
    return redirect('viewcriminals')

def permemantdelete(request,id):
    search = criminal.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    
def restore(request,id):
    search=criminal.objects.get(id=id)
    search.deleted=False
    search.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
