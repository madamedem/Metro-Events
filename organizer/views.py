from django.contrib import messages

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib import messages
from django.http import HttpResponseRedirect, request





from django.contrib.auth.models import auth
from django.contrib.auth import login, logout

from .forms import *
from .models import *


# Create your views here.

def destroy(request, id):  
    Event = Event.objects.get(id=id)  
    Event.delete()  

    return redirect("organizer:organizer_events")


class organizerIndexView(View):
    template_name="organizer-dashboard.html"

    def get(self,request):
        events = Event.objects.all()
        return render(request,self.template_name, {'event': events})


class organizerEventsView(View):
    template_name="organizer-events.html"

    def get(self,request):
        events = Event.objects.all()
        return render(request,self.template_name, {'event': events})

    def post(self,request):
        if request.method == "POST":
            if 'btn_delete' in request.POST:  
                event_id = request.POST.get('event_id')

        del_event = Event.objects.filter(event_id = event_id)
        del_event.delete()

        context ={
                'del_event': del_event
        }

        return render("organizer-events.html", context)


class organizerEventsAddView(View):

    def get(self,request):
        formEvent = EventCreationForm()
        return render(request, 'organizer-eventsAdd.html', {'formEvent': formEvent})
        
    def post(self,request):
        event_name = request.POST.get('event_name')
        event_description = request.POST.get('event_description')
        event_type = request.POST.get('event_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        print(event_name)
        print(event_description)
        print(event_type)
        print(start_date)
        print(end_date)
        print(start_time)
        print(end_time)

        event = Event(event_name=event_name, event_description=event_description, 
                event_type=event_type, start_date=start_date, end_date=end_date,
                start_time=start_time, end_time=end_time
                 )
        event.save()

        context ={
                'event': event
        }

        return render(request, "organizer-eventsAdd.html" , context)

class organizerProfileView(View):
    template_name="organizer-profile.html"

    def get(self,request):
        return render(request,self.template_name)

class organizerReviewView(View):
    template_name="organizer-review.html"

    def get(self,request):
        return render(request,self.template_name)