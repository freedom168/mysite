__author__ = 'passerby'
from django.shortcuts import *
from django.core.mail import send_mail
from smtplib import SMTPException
import os

def sendMail():
    print('---------------start send---------------')
    try:
        send_mail('[test django]', 'hello', 'googolplex_alaph@126.com', ['569078986@qq.com'], fail_silently=False)
    except SMTPException:
        print('error')
    print('----------------end send----------------')

def download_excel(request):
    filename = './excel/test.txt'
    f = open(filename,'rb')
    data = f.read()
    f.close()
    return HttpResponse(data)

def index(request):
    return render(request, 'mysite/index.html', {})