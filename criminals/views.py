from django.shortcuts import redirect,render,HttpResponse
from criminals import views
from .form import *
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models  import *
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


@adminOnly
# @permission_required('criminals.delete_crime')
def home(request):
    criminals= criminal.objects.all()
    return render(request,'index.html',{'criminal':criminals})


@csrf_exempt
@adminOnly
def addcriminal(request):
    # criminal_form = CriminalForm(request.POST or None, request.FILES or None)
    # crime_form = CrimeForm(request.POST or None, request.FILES or None)
    # doc_form = DocumentsForm(request.POST or None, request.FILES or None)
    # if criminal_form.is_valid():
    #     criminal_form.save()

    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        height=request.POST.get('height')
        gender=address=request.POST.get('gender')
        martialstatus=request.POST.get('martialstatus')
        address=request.POST.get('address')
        lang=request.POST.get('lang')
        identify=request.POST.get('identify')
        status=request.POST.get('status')
        dob=request.POST.get('dob')

        file = request.FILES.get('file')
        if file:
            print('picture uploaded successfully')
            print(request.FILES)
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            print('filename is ',filename)
            url = fs.url(filename)
            print(url)

            user= criminal(fname=fname,lname=lname,email=email,contact_no=phone,dob=dob,height=height,
            language=lang,martial_status=martialstatus,residence=address,status=status,
            identification=identify,sex=gender,profile_pic=filename)
            # user.save()
        else:
            data=request.POST.get('webcamimg')
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            print('extension is  :',ext)
            data = ContentFile(base64.b64decode(imgstr), name='webcamimage.'+ ext)
            
            user= criminal(fname=fname,lname=lname,email=email,contact_no=phone,dob=dob,height=height,
            language=lang,martial_status=martialstatus,residence=address,status=status,
            identification=identify,sex=gender,profile_pic=data)
            user.save()
        
    return render(request,'addcriminal.html')

@adminOnly
def viewcriminal(request,id):
    criminals=criminal.objects.get(id=id)
    return render(request,'criminal.html',{'criminal':criminals})

@csrf_exempt
def docs(request,id):
    crim=criminal.objects.get(id=id)
    dform=DocumentsForm(request.POST or None, request.FILES or None)
    if dform.is_valid():
        dform.save()
    if request.method=="POST":
        webvideo.objects.create(vid=request.POST.get('vid'))
    return render(request,'viewdocs.html',{'criminal':crim,'form':dform})

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
    cform=CriminalForm(request.POST or None, request.FILES or None,instance=person)
    if cform.is_valid():
        cform.save()

    return render(request,'editcriminal.html',{'cform':cform})

@adminOnly
def updateprofile(request,id):
    return render(request,'updateprofile.html')


def userlogin(request):
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