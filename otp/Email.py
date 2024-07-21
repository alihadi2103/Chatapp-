from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage 
from django.conf import settings
import smtplib
from email.mime.text import MIMEText

def send_otp_password(email,username,otp_password):
    
    
    context={
        "name":username,
        " otp_password":otp_password,
        }
    
    email_subject='this is otp pasword to confirm your eamail and complete your signup processe'
    eamil_body=render_to_string("otp_password_message.txt",context)
    email_ob=EmailMessage(from_email=settings.DEFAULT_FROM_EMAIL,subject=email_subject,body=eamil_body,to=[email])
    return email_ob.send(fail_silently=False)





# SMTP settings
import smtplib
from email.mime.text import MIMEText

def send_otp_with_smtp(username, email, otp):
    if not all([username, email, otp]):
        print("Username, email, and OTP are required")
        return
    
    # Configuring the SMTP connection
    user = "alihadi210403@gmail.com"
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = user
    smtp_password = 'kiprzvlfhqnrgzgq'  # App-specific password

    # Email details
    from_email = smtp_user
    to_email = email
    subject = 'OTP confirmation'
    body = f'Hello {username}, this is your OTP password: {otp}. Thanks for signing up.'

    # Create MIMEText email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Send email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, [to_email], msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")




    
    