from django.urls import path
from . import views

urlpatterns = [
    path('create_job', views.create_job, name='create_job'),
    path('update_job<int:pk>/', views.update_job, name='update_job'),
    path('job_listing', views.job_listing, name='job_listing'),
]