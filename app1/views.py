from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Register
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def login(request):
    return render(request,'login.html')
def logincheck(request):
    email1=request.GET['email']
    password1=request.GET['password']
    try:
        r=Register.objects.get(email=email1,password=password1)
    except Exception as ex:
        return render(request,'login.html',{'msg':'invalid'}) 
    return render(request,'room.html')
    

def register(request):
    return render(request,'register.html')
def contact(request):
    return render(request,'contact.html')
def doregister(request):
    fullname=request.GET['fullname']
    email=request.GET['email']
    password=request.GET['password']
    phone=request.GET['phone']
    r=Register()
    r.fullname=fullname
    r.email=email
    r.password=password
    r.phone=phone
    r.save()
    return render(request,'register.html',{"msg":'Registration Successful'})
def logincheck(request):
    email=request.GET['email']
    password=request.GET['password']
    r=None
    try:
       r=Register.objects.get(email=email,password=password)
       print("r=",r)
    except Exception as ex:
        print(ex)
        return render(request,"login.html",{"msg":"invalid emailid/password"})  
    if(r!=None):
        if(r.desig=='user'):
            return redirect('/userhome')
        if(r.desig=='admin'):
            return redirect('/adminhome')
        else:
            return render(request,"room.html",{"msg":"invalid designation"})
def userhome(request):
    return render(request,'userhome.html')
def adminhome(request):
    return render(request,'adminhome.html')

def viewusers(request):
    users=Register.objects.all()
    return render(request,'viewusers.html',{'users':users})
def modify(request):
    operation=request.GET['operation']
    print(operation)
    fullname=request.GET['fullname']
    email=request.GET['email']
    password=request.GET['password']
    desig=request.GET['desig']
    r=Register.objects.get(email=email)
    if operation=="update":
       r.fullname=fullname
       r.email=email
       r.password=password
       r.desig=desig
       r.save()
    else:
        Register.delete(r)
    users=Register.objects.all()
    return render(request,"viewusers.html",{"users":Register.objects.all()})