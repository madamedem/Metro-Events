from django.urls import path
from . import views

app_name = 'organizer'

urlpatterns = [
    path('organizerIndex', views.organizerIndexView.as_view(), name='organizer_index'),
    path('organizerEvents', views.organizerEventsView.as_view(), name='organizer_events'),
    path('organizerReview', views.organizerReviewView.as_view(), name='organizer_review'),
    path('organizerProfile', views.organizerProfileView.as_view(), name='organizer_profile'),
    path('organizerLogin', views.organizerLoginView.as_view(), name='organizer_login'),
    path('organizerHomePage', views.organizerLoggedInView.as_view(), name="organizer_homepage"),
]