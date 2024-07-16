from django.shortcuts import render, redirect
from .Forms import SignupForm, OtpForm
from .tasks import generate_otp_password,send_otp_email,count_down
from django.contrib.auth.models import User

# Create your views here.
def sign_up_veiw(request):
    form=SignupForm
    if request.method == 'POST':
        form=form(request.POST)
        if form.is_valid():
            user_username=form.cleaned_data["Username"]
            user_email=form.cleaned_data["Email"]
            user_password=form.cleaned_data["Password"]
            user=User.objects.create_user(username=user_username, email=user_email, password=user_password)
            id=user.id
            return redirect(request,url="otp_check/<int>:id /<str>:user_email/")
    else:
        
        form=form()
        
        return render(request,"signup.html",{'form':form})
    
    
def check_user(request,id,email):
    
    form=OtpForm
    user=User.objects.get(id=id,eamail=email)
    username=user.username
    if request.method=='GET':
        countdown=count_down().aply_async()
        pas=generate_otp_password.aply_async(count=countdown)
        send_otp_email.aply_async(eamail=email,otp_password=pas,username=username)
        
        return render(request,"otp.html",{'countdown':countdown,'form':form,})
    elif request.method =="POST":
        if request.data ==None :
            otp_pass=generate_otp_password.aply_async()
            send_otp_email.aply_async(eamail=email,otp_password=generate_otp_password.aply_async(),username=username)
            countdown=count_down().aply_async()
            form=form(request.Post)
            return render(request,"otp.html",{'countdown':countdown,'form':form,})
        else:
            form=form(request.Post)
            if form.is_valid():
                otp=form["otp_password"]
                if otp == otp_pass:
                    user.save()
                    return redirect(request,"login.html","login/")
            
            
            
    
            
        
    
    #handling the task:
    
    
    
    
    
    

    
    
            
            
            
        
    