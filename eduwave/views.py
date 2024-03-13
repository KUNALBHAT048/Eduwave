from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request,'base.html')

def HOME(request):
    return render(request,"main/home.html")

def single_course(request):
    return render(request,'main/single_course.html')



@login_required(login_url='/login')
def ho(request):
    return render(request,"main/afterlogin.html")

