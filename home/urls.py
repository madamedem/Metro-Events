from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('generalHome', views.generalHomeView.as_view(), name='general_home'),
    path('generalEvents', views.generalEventsView.as_view(), name='general_events'),
    path('generalCategory', views.generalCategoryView.as_view(), name='general_category'),
    path('generalAbout', views.generalAboutView.as_view(), name='general_about'),
]