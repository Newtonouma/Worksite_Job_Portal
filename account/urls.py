from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("register_applicant", views.register, name='register_applicant'),
    path("register_recruiter/", views.register_recruiter, name='register_recruiter'),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name='logout')
    
]