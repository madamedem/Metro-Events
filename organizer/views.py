from django.contrib import messages

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib import messages


from django.contrib.auth.models import auth
from django.contrib.auth import login, logout

from .forms import *
from .models import *


# Create your views here.

class organizerIndexView(View):
    template_name="organizer-dashboard.html"

    def get(self,request):
        return render(request,self.template_name)


class organizerEventsView(View):
    template_name="organizer-events.html"

    def get(self,request):
        return render(request,self.template_name)

class organizerEventsAddView(View):
    template_name="organizer-eventsAdd.html"

    def get(self,request):
        formEvent = EventCreationForm()
        return render(request,self.template_name, {'formEvent': formEvent})
        
class organizerProfileView(View):
    template_name="organizer-profile.html"

    def get(self,request):
        return render(request,self.template_name)

class organizerReviewView(View):
    template_name="organizer-review.html"

    def get(self,request):
        return render(request,self.template_name)