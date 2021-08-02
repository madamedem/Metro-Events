from django.contrib import messages

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib import messages



# Create your views here.

class adminHomeView(View):
    template_name="admin.html"

    def get(self,request):
        return render(request,self.template_name)

class adminViewRequest(View):
    template_name="admin-request.html"

    def get(self,request):
        return render(request,self.template_name)

class adminViewUserRequest(View):
    template_name="admin-view.html"

    def get(self,request):
        return render(request,self.template_name)

class adminAcceptRequest(View):
    template_name="admin-notif-success.html"

    def get(self,request):
        return render(request,self.template_name)
    
class adminDenyRequest(View):
    template_name="admin-notif-deny.html"

    def get(self,request):
        return render(request,self.template_name)