from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from models import *


import simplejson as json


# Create your views here.
class UserIndex(View):

    def get(self, request):

        return render(request, 'accounts/login.html', {'title': 'D4 Networks Login'})

    def post(self, request):

        try:
            is_validate = authenticate(username=request.POST['username'], password=request.POST['password'])
            if is_validate:
                login(request, is_validate)
                # return redirect('/user/')
                return HttpResponse(json.dumps({'status': True}))
            else:
                return HttpResponse(json.dumps({'status': False}))
        except IndexError:
            return False


# Dashboard view with existing VM's
class UserDashboard(View):

    method_decorator(login_required)

    def get(self, request):

        list_vms = VMS.objects.list_all_vms(request.user.id)
        return render(request, 'accounts/dashboard.html', {'title': 'Dashboard', 'vms': list_vms })

    method_decorator(login_required)

    def post(self, request):

        return HttpResponse(json.dumps({'status': True}))


#User profile setings view
class UserProfileSettings(View):

    method_decorator(login_required)
    def get(self, request):
        user_profile = None
        try:
            user_profle = Profile.objects.filter(user_id=request.user.id)[0]
        except IndexError:
            user_profile = None
            pass
        return render(request, 'accounts/profile/settings.html', {'title': 'Settings', 'user': request.user,
                                                                  'user_profile': user_profile })

    method_decorator(login_required)
    def post(self, request):
        if request.POST['first_name'] is None or request.POST['first_name'] == '':
            return HttpResponse(json.dumps({'status': 'Please Enter Your First Name'}))
        if request.POST['last_name'] is None or request.POST['last_name'] == '':
            return HttpResponse(json.dumps({'status': 'Please Enter Your Last Name'}))
        User.objects.filter(id=request.user.id).update(first_name=request.POST['first_name'],last_name=request.POST['last_name'])
        try:
            Profile.objects.filter(user_id=request.user.id).update(company=request.POST['company'])
        except IndexError:
            pass
        return HttpResponse(json.dumps({'status': True}))


class UserLogout(View):

    def get(self, request):
        logout(request)
        return redirect('/user/login/')

# VMS action against user


def vm_start(request):

    if request.POST['vm_id'].isdigit():
        if not Commands.objects.is_command_exist(request.POST['vm_id']): # if the user already command does not exist already
            node = VMS.objects.vm_node(request.POST['vm_id'], request.user.id)
        else:
            return HttpResponse(json.dumps({'status':'Command Already Exists'}))
    else:
        return HttpResponse(json.dumps({'status':'Invalid Virtual Machine ID Passed'}))
    Commands(node_id=node.node_id,vm_id=request.POST['vm_id'], action='Start').save()
    return HttpResponse(json.dumps({'status':'Virtual Machine Successfully Started'}))


def vm_pause(request):

    if request.POST['vm_id'].isdigit():
        if not Commands.objects.is_command_exist(request.POST['vm_id']): # if the user already command does not exist already
            node = VMS.objects.vm_node(request.POST['vm_id'], request.user.id)
        else:
            return HttpResponse(json.dumps({'status':'Command Already Exists'}))
        node = VMS.objects.vm_node(request.POST['vm_id'], request.user.id)
    else:
        return HttpResponse(json.dumps({'status':'Invalid Virtual Machine ID Passed'}))
    Commands(node_id=node.node_id,vm_id=request.POST['vm_id'], action='Pause').save()
    return HttpResponse(json.dumps({'status':'Virtual Machine Successfully Paused'}))

def vm_shutdown(request):

    if request.POST['vm_id'].isdigit():
        if not Commands.objects.is_command_exist(request.POST['vm_id']): # if the user already command does not exist already
            node = VMS.objects.vm_node(request.POST['vm_id'], request.user.id)
        else:
            return HttpResponse(json.dumps({'status':'Command Already Exists'}))
        node = VMS.objects.vm_node(request.POST['vm_id'], request.user.id)
    else:
        return HttpResponse(json.dumps({'status':'Invalid Virtual Machine ID Passed'}))
    Commands(node_id=node.node_id,vm_id=request.POST['vm_id'], action='Shutdown').save()
    return HttpResponse(json.dumps({'status':'Virtual Machine Successfully Shutdown'}))


def vm_reboot(request):

    if request.POST['vm_id'].isdigit():
        if not Commands.objects.is_command_exist(request.POST['vm_id']): # if the user already command does not exist already
            node = VMS.objects.vm_node(request.POST['vm_id'], request.user.id)
        else:
            return HttpResponse(json.dumps({'status':'Command Already Exists'}))
        node = VMS.objects.vm_node(request.POST['vm_id'], request.user.id)
    else:
        return HttpResponse(json.dumps({'status':'Invalid Virtual Machine ID Passed'}))
    Commands(node_id=node.node_id,vm_id=request.POST['vm_id'], action='Reboot').save()
    return HttpResponse(json.dumps({'status':'Virtual Machine Successfully Rebooted'}))
