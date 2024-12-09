from django.urls import path
from . import views



urlpatterns = [
    path('create_job', views.create_job, name='create_job'),
    path('update_job<int:pk>/', views.update_job, name='update_job'),
    path('job_listing', views.job_listing, name='job_listing'),
    path('manage_jobs', views.manage_jobs, name='manage_jobs'),
    path('jobs/<int:pk>/edit/', views.edit_job, name='edit_job'),
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('job/<int:job_id>/applicants/', views.view_applicants, name='view_applicants'),
]