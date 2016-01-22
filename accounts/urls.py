__author__ = 'azhar'
from django.conf.urls import url
from django.conf.urls import patterns
from views import *

urlpatterns = patterns(
    url(r'', UserIndex.as_view()),
    url(r'^$', UserDashboard.as_view()),
    url(r'^login/$', UserIndex.as_view()),
    url(r'^vm_start/$', vm_start),
    url(r'^vm_pause/$', vm_pause),
    url(r'^vm_reboot/$', vm_reboot),
    url(r'^vm_shutdown/$', vm_shutdown),
    url(r'^logout/$', UserLogout.as_view()),

)