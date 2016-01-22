__author__ = 'azhar'
from django.conf.urls import url
from django.conf.urls import patterns
from views import *

urlpatterns = patterns(
    url(r'', UserIndex.as_view()),
    url(r'^$', UserDashboard.as_view()),
    url(r'^login/$', UserIndex.as_view()),
)