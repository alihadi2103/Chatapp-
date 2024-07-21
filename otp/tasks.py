from OTPA.celery import app
import random
import time
import datetime
from celery import shared_task
from .Email import send_otp_password ,  send_otp_with_smtp
from pyotp.hotp import HOTP
from pyotp.totp import TOTP





def generate_otp_password( interval):
    
    otp_handler=TOTP('base32secret3232',digits=8,interval=interval)
    otp_pass=otp_handler.now()
    start_time=time.time()
    elapsed_time = time.time() - start_time
    print(f"OTP generated in  {elapsed_time}     seconds.")
    print(f"elapsed time: {elapsed_time}")
    return otp_pass


@shared_task()
def send_otp_email(email,username,otp_password):
    if otp_password is not None:
        start_time=time.time()
       
        k=send_otp_password(email,username,otp_password)
        
        
        
        elapsed_time = time.time() - start_time
        
        return bool(k)
    
@shared_task()
def send_otp (username, email, otp):
    
        
        if otp is not None:
            start_time = time.time()
            
            
            result = send_otp_with_smtp(username=username, email=email, otp=otp)
            
            elapsed_time = time.time() - start_time
            
            return result
        
        raise
@shared_task()
def add(a,b):
    
    return a+b
    