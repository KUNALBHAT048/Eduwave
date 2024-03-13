from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .forms import CustomRegistrationForm
from django.contrib.auth import authenticate ,login
from app.models import UserProfile

def reg(request):
    if request.method == "POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()            
            login(request,user)
            return redirect('/afterlogin')  # Redirect to a new URL, adjust as 
            # return  HttpResponse("Registered Successfully! You can now login.")
        else:
            # If the form is not valid, the errors will be displayed in the form template
            print(register_form.errors)  # Optional: Log form errors
    else:
        register_form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'register_form': register_form})
    # return HttpResponse("not created yet")
