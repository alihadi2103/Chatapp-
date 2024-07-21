import smtplib
from email.mime.text import MIMEText
import datetime 
import time


# SMTP settings
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






smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'alihadi210403@gmail.com'
smtp_password = 'kiprzvlfhqnrgzgq'  # App-specific password

# Email details
from_email = smtp_user
to_email = 'alihadi2103@gmail.com'
subject = 'Test Email'
otp=generate_otp_password(interval=300)

body = f'This is a test email for {otp}.'

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
