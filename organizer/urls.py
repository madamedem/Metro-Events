from django.urls import path
from . import views

app_name = 'organizer'

urlpatterns = [
    path('organizerHome', views.organizerHomeView.as_view(), name='organizer_home'),
    path('organizerEvents', views.organizerEventsView.as_view(), name='organizer_events'),
    path('organizerReview', views.organizerReviewView.as_view(), name='organizer_review'),
    path('organizerProfile', views.organizerProfileView.as_view(), name='organizer_profile'),
    path('organizerLogin', views.organizerLoginView.as_view(), name='organizer_login'),
    path('organizerHomePage', views.organizerLoggedInView.as_view(), name="organizer_homepage"),
]