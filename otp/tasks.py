from OTPA.celery import app
import random
import time
import datetime
from celery import shared_task
from .Email import send_otp_password
from pyotp.hotp import HOTP
from pyotp.totp import TOTP


@shared_task()
def generate_otp_password( interval):
    otp_handler=TOTP('base32secret3232',digits=8,interval=interval)
    otp_pass=otp_handler.now()
    return otp_pass


@shared_task()
def send_otp_email(email,username,otp_password):
    if otp_password is not None:
        return send_otp_password(email,username,otp_password)
