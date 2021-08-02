from django import forms
from .models import *


class EventCreationForm(forms.ModelForm):

   
        class Meta:
            model = Event
            fields = ('event_name', 'event_description', 'event_type', 'start_date', 'end_date',
                    'start_time', 'end_time')


class ReviewCreationForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ('title', 'content', 'rating')