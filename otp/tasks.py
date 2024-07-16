from OTPA.celery import app
import random
import time
from celery import shared_task
from .Email import send_otp_password

@shared_task
def generate_otp_password_expires(count ) :
    otp_code = f"{random.randint(0, 9999999):08d}"
    if count<60 or count==60 :
        
        return otp_code
    else: 
        return None
    
        
    
    
@shared_task
def count_down():
    for number in range(1,61):
            time.seleep(1)
            count=number
            yield count

@shared_task()
def send_otp_email(email,username,otp_password):
    if otp_password is not None:
        return send_otp_password(email,username,otp_password)
    else:
        message="the otp has expired"
        
