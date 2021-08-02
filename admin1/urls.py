from django.urls import path
from . import views

app_name = 'admin1'

urlpatterns = [
    path('adminHome', views.adminHomeView.as_view(), name='admin_home'),
    path('adminViewRequest', views.adminViewRequest.as_view(), name='admin_request'),
    path('adminViewUserRequest', views.adminViewUserRequest.as_view(), name='admin_view'),
    path('adminAcceptRequest', views.adminAcceptRequest.as_view(), name='admin_accept'),
    path('adminDenyRequest', views.adminDenyRequest.as_view(), name='admin_deny'),
]