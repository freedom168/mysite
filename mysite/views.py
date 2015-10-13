__author__ = 'passerby'
from django.shortcuts import *
from django.core.mail import send_mail
from smtplib import SMTPException
# from django.template import Context, loader


def sendMail():
    print('---------------start send---------------')
    try:
        send_mail('subject', 'this is the message of email', 'spasserby78@gmail.com', ['569078986@qq.com'], fail_silently=False)
    except SMTPException:
        print(SMTPException)
        print('error')
    print('----------------end send----------------')



def index(request):
    sendMail()
    return render(request, 'mysite/index.html', {})