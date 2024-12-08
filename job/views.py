from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job
from .forms import CreateJobForm, UpdateJobForm    
from django.contrib.auth.models import Group


def create_job(request):
    user = request.user
    is_recruiter = user.groups.filter(name='Recruiter').exists()
    has_company = hasattr(user, 'company') and user.company is not None

    if is_recruiter and has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                var.save()
                messages.info(request, 'New Job has been created')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Something went wrong with the form')
                return redirect('create_job')
        else:
            form = CreateJobForm()
            context = {'form': form}
            return render(request, 'job/create_job.html', context)
    else:
        messages.warning(request, 'You cannot create a job. Ensure you are a recruiter and have a company.')
        return redirect('dashboard')

    


def update_job(request, pk):
    job = Job.object.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Job details have been successfully Updated')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = UpdateJobForm(instance=job)
        context = {'form': form}
        return render(request, 'job/update_job.html', context)

from django.shortcuts import render
from .models import Job

def job_listing(request):
    jobs = Job.objects.filter(is_available=True)  # Fetch only available jobs
    return render(request, 'job/job_listing.html', {'jobs': jobs})
