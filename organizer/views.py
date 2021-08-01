from django.contrib import messages

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout

from .forms import OrganizerForm, LoginForm, AccountForm
from .models import Account, Organizer



# Create your views here.

class organizerHomeView(View):
    template_name="organizer-dashboard.html"

    def get(self,request):
        return render(request,self.template_name)

class organizerLoginView(View):
    template_name="organizer-login.html"

    def get(self,request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        print("Username:" + uname)
        error = ""
        print("No of record:" + str(Account.objects.filter(pk=uname).count()))
        

        if Account.objects.filter(pk=uname).count() != 0:
            account = Account.objects.get(pk=uname)
            if account.password == pwd:
                print("username" + uname)

                return redirect(reverse('organizer:organizer_homeaccount', kwargs={'uname': uname, }))
            else:
                error = "Incorrect password."
        else:
            error = "Username does not exist."

        return render(request, self.template_name, {'form': form, 'error': error}) 

 
class organizerLoggedInView(View):
    template_name = "organizer-dashboard.html"

    def get(self, request, uname):

        print(uname)
        return render(request, self.template_name, {'uname': uname})





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