from django.shortcuts import render

    
from django.contrib.auth.models import Group

def dashboard(request):
    user = request.user
    is_applicant = user.groups.filter(name='Applicant').exists()
    is_recruiter = user.groups.filter(name='Recruiter').exists()

    context = {
        'is_applicant': is_applicant,
        'is_recruiter': is_recruiter,
        'items': [] 
    }
    return render(request, 'dashboard/dashboard.html', context)
