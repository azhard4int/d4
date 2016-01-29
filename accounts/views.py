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


class UserDashboard(View):

    method_decorator(login_required)

    def get(self, request):

        list_vms = VMS.objects.list_all_vms(request.user.id)
        return render(request, 'accounts/dashboard.html', {'title': 'Dashboard', 'vms': list_vms })

    method_decorator(login_required)

    def post(self, request):

        return HttpResponse(json.dumps({'status': True}))


class UserLogout(View):

    def get(self, request):
        logout(request)
        return redirect('/user/login/')

# VMS action against user


def vm_start(request):

    if request.POST['vm_id'].isdigit():
        if not Commands.objects.is_command_exist(request.POST['vm_id']):
            node = VMS.objects.vm_node(request.POST['vm_id'], request.user.id)
        else:
            return HttpResponse(json.dumps({'status':'Command Already Exists'}))
    else:
        return HttpResponse(json.dumps({'status':'Invalid Virtual Machine ID Passed'}))
    Commands(node_id=node.node_id,vm_id=request.POST['vm_id'], action='Start').save()
    return HttpResponse(json.dumps({'status':'Virtual Machine Successfully Started'}))


def vm_pause(request):

    if request.POST['vm_id'].isdigit():
        if not Commands.objects.is_command_exist(request.POST['vm_id']):
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
        if not Commands.objects.is_command_exist(request.POST['vm_id']):
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
        if not Commands.objects.is_command_exist(request.POST['vm_id']):
            node = VMS.objects.vm_node(request.POST['vm_id'], request.user.id)
        else:
            return HttpResponse(json.dumps({'status':'Command Already Exists'}))
        node = VMS.objects.vm_node(request.POST['vm_id'], request.user.id)
    else:
        return HttpResponse(json.dumps({'status':'Invalid Virtual Machine ID Passed'}))
    Commands(node_id=node.node_id,vm_id=request.POST['vm_id'], action='Reboot').save()
    return HttpResponse(json.dumps({'status':'Virtual Machine Successfully Rebooted'}))
