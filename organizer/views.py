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

    def get(self,request):
        return render(request, 'organizer-login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        

        if user is not None:
            auth.login(request, user)
            is_organizer = Organizer.objects.filter(user_id=request.user.id)

            if is_organizer:
                return redirect('organizer:organizer_homepage')

            else:
                messages.error(request,"Your account is unauthorized to log in.")
                return redirect("organizer:organizer_login")   

        else:
            messages.error(request, 'Invalid username or password.')
            return redirect("organizer:organizer_login")
 
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