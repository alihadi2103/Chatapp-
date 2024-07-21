#django imports
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
#application import
from .Forms import SignupForm, OtpForm
from .tasks import generate_otp_password,send_otp_email,send_otp

#other dependecies
import time
import datetime

# Sign up view the crete a session to validate the user credentials befor saving it
from django.shortcuts import render, redirect
from django.urls import reverse
import asyncio

def sign_up_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user_username = form.cleaned_data["username"]
            user_email = form.cleaned_data["email"]
            user_password = form.cleaned_data["password"]
            
            # Store user data in the session
            request.session["username"] = user_username
            request.session["email"] = user_email  # Fixed typo here
            request.session["password"] = user_password
            
            # Redirect to the check_user_url (make sure to use the correct URL name)
            return redirect(reverse("check_user_url"))
    else:
        form = SignupForm()  # Instantiate form for GET request

    return render(request, "signup.html", {'form': form})

    
def check_user(request):
    
    form=OtpForm()
   
    username=request.session["username"]
    email=request.session["email"]
    password=request.session["password"]
    print("the username in the session is ",username)
    print("the email in the session is ",email)
    print("the password in the session is ",password)
    
    massage=None
    if request.method=='GET':
        
        otp= generate_otp_password(interval=90)
        
        
        print("the otpis is:",otp)
        request.session["otp"]=otp
        print("="*100)
        print("sending email has started")
        send_otp.apply_async([username,email,otp])
        print("sending email has finished")
        print("="*100)
        print("the session otp",request.session["otp"])
        
        message="an email associated with an Otp , Be Carfull the otp will expire after 90 seconds  "
        
        return render(request,"check_user.html",{'form':form,message:message})
    if  request.method=='POST':
        
        new_otp=otp= generate_otp_password(interval=90)
        form=form(request.Post)
        form.is_valid()
        otp_passed=form.cleandata["otp_password"]
        if otp_passed==request.session["otp"]:
            user=User.objects.create_user(username=username,password=password,email=email).save()
            message=''' your has signup process has been successful and you can login in now'''
            redirect(request,{"message":message},reverse("login_url"))
            
        else:
            message=''' your has signup process has been unsuccessful, it seems the you otp has expired'''
            return render(request,"check_user.html",{'form':form,"message":message})
        
def sign_in(request):
    return render(request,"signin.html")