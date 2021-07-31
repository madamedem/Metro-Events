from django.contrib import messages

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib import messages

# Create your views here.

class generalHomeView(View):
    template_name="general-home.html"

    def get(self,request):
        return render(request,self.template_name)

class generalEventsView(View):
    template_name="general-events.html"

    def get(self,request):
        return render(request,self.template_name)


class generalCategoryView(View):
    template_name="general-category.html"

    def get(self,request):
        return render(request,self.template_name)


class generalAboutView(View):
    template_name="general-about.html"

    def get(self,request):
        return render(request,self.template_name)

