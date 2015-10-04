__author__ = 'passerby'
from django.conf.urls import patterns, url

urlpatterns = patterns('polls.views',
    url(r'^$', 'index'),
)