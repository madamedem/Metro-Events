from django.contrib import messages

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib import messages



# Create your views here.

class organizerHomeView(View):
    template_name="organizer-dashboard.html"

    def get(self,request):
        return render(request,self.template_name)

class organizerEventsView(View):
    template_name="organizer-events.html"

    def get(self,request):
        return render(request,self.template_name)
        
class organizerProfileView(View):
    template_name="organizer-profile.html"

    def get(self,request):
        return render(request,self.template_name)

class organizerReviewView(View):
    template_name="organizer-review.html"

    def get(self,request):
        return render(request,self.template_name)