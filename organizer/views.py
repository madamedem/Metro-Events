from django.contrib import messages

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout

from .forms import OrganizerForm, LoginForm
from .models import Account, Organizer



# Create your views here.

class organizerLoginView(View):
    template_name="organizer-login.html"

    def get(self,request):
        formLogin = LoginForm()
        return render(request, self.template_name, {'formLogin': formLogin})

    def post(self, request):
        formLogin = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Username:" + username)
        error = ""
        print("No of record:" + str(Account.objects.filter(pk=username).count()))
        

        if Account.objects.filter(pk=username).count() != 0:
            account = Account.objects.get(pk=username)
            if account.password == password:
                print("username" + username)

                return redirect(reverse('organizer:organizer_account', kwargs={'username': username, }))
            else:
                error = "Incorrect password."
        else:
            error = "Username does not exist."

        return render(request, self.template_name, {'formLogin': formLogin, 'error': error}) 

 
class organizerLoggedInView(View):
    template_name = "organizer-dashboard.html"

    def get(self, request, username):

        print(username)
        return render(request, self.template_name, {'username': username})





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