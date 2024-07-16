from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .Forms import SignupForm, OtpForm
from .tasks import generate_otp_password,send_otp_email

import time
import datetime

# Create your views here.
def sign_up_veiw(request):
    form=SignupForm
    if request.method == 'POST':
        form=form(request.POST)
        if form.is_valid():
            
            
            user_username=form.cleaned_data["Username"]
            user_email=form.cleaned_data["Email"]
            user_password=form.cleaned_data["Password"]
            
            request.session["username"]=user_username
            request.session["eamail"]=user_password
            request.session["password"]=user_password
            
            return redirect(request,url="check_user/")
    else:
        
        form=form()
        
        return render(request,"signup.html",{'form':form})
    
    
def check_user(request):
    
    form=OtpForm
    username=request.session.username
    email=request.session.email
    password=request.session.password
    
    if request.method=='GET':
        
        otp= generate_otp_password.aply_async(time,interval=60).get()
        send_otp_email(email,username,otp)
        request.session["otp"]=otp
        print (request.otp)
        
        return render(request,"check_user.html",{'form':form})
    if  request.method=='POST':
        
        new_otp=otp= generate_otp_password.aply_async(interval=90).get()
        form=form(request.Post)
        form.is_valid()
        otp_passed=form.cleandata["otp_password"]
        if otp_passed==request.session["otp"]:
            user=User.objects.create_user(username=username,password=password,email=email).save()
            redirect(request,"login.html","/login/")
        
        
    
    #handling the task:
    
    
    
    
    
    

    
    
            
            
            
        
    