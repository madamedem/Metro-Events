from django.urls import path
from . import views

app_name = 'organizer'

urlpatterns = [
    path('organizerHome', views.organizerHomeView.as_view(), name='organizer_home'),

]