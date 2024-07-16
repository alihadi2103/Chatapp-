#django imports
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
#application import
from .Forms import SignupForm, OtpForm
from .tasks import generate_otp_password,send_otp_email

#other dependecies
import time
import datetime

# Sign up view the crete a session to validate the user credentials befor saving it
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
    massage=None
    if request.method=='GET':
        
        otp= generate_otp_password.aply_async(time,interval=60).get()
        send_otp_email(email,username,otp)
        request.session["otp"]=otp
        message="an email associated with an Otp , Be Carfull the otp will expire after 90 seconds  "
        
        return render(request,"check_user.html",{'form':form,message:message})
    if  request.method=='POST':
        
        new_otp=otp= generate_otp_password.aply_async(interval=90).get()
        form=form(request.Post)
        form.is_valid()
        otp_passed=form.cleandata["otp_password"]
        if otp_passed==request.session["otp"]:
            user=User.objects.create_user(username=username,password=password,email=email).save()
            message=''' your has signup process has been successful and you can login in now'''
            redirect(request,"login.html","/login/",{"form":form,"message":message},)
            
        else:
            message=''' your has signup process has been unsuccessful, it seems the you otp has expired'''
            return render(request,"check_user.html",{'form':form,"message":message})