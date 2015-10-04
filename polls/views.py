__author__ = 'passerby'
from django.http import HttpResponse
from django.shortcuts import render
def index(requeset):
    return render(requeset, 'polls/index.html', {})