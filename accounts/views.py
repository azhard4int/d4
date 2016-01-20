from django.shortcuts import HttpResponse, render
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

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
            else:
                return HttpResponse(json.dumps({'status': False}))
        except IndexError:
            return False