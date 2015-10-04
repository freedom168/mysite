__author__ = 'passerby'
from django.shortcuts import *
def index(request):
    return render(request, 'mysite/index.html', {})