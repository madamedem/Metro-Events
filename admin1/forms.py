from django import forms
from .models import *


class BecomeOrganizer(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ('organizerID')