from django.shortcuts import render,redirect

def base(request):
    return render(request,'base.html')

def HOME(request):
    return render(request,"main/home.html")

def single_course(request):
    return render(request,'main/single_course.html')

def ho(request):
    return render(request,"main/afterlogin.html")