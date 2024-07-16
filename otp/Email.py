from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core import settings


def send_otp_password(email,username,otp_password):
    
    
    context={
        "name":username,
        " otp_password":otp_password,
        }
    
    email_subject='''thank you for singing up with us, this precijer to confirm your eamail and completing you signup
                    this is otp pasword to confirm your eamail and complete your signup'''
    eamil_body=render_to_string("otp_password_message.txt",context)
    email_ob=EmailMessage(settings.DEFAULT_FROM_EMAIL,[email,],email_subject=email_subject,email_body=eamil_body,)
    return email_ob.send(fail_silently=False)
    
    