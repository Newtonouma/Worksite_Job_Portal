from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib import messages
from .models import Job, JobApplication
from .forms import CreateJobForm, UpdateJobForm , JobForm, JobApplicationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

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
    
def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs': jobs}  # Use 'jobs' to match the template's key
    return render(request, 'job/manage_jobs.html', context)



def job_listing(request):
    jobs = Job.objects.filter(is_available=True)  # Fetch only available jobs
    return render(request, 'job/job_listing.html', {'jobs': jobs})



def edit_job(request, pk):
    job = get_object_or_404(Job, pk=pk, user=request.user)  # Ensure only the creator can edit
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('manage_jobs')  # Redirect to the manage jobs page
    else:
        form = JobForm(instance=job)
    
    return render(request, 'job/edit_job.html', {'form': form, 'job': job})


@login_required
def apply_for_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    # Check if the user has already applied for the job
    if JobApplication.objects.filter(applicant=request.user, job=job).exists():
        messages.info(request, "You have already applied for this job.")
        return redirect('job_listing')
    
    # Create the job application
    application = JobApplication(applicant=request.user, job=job)
    application.save()

    messages.success(request, f"You have successfully applied for the job: {job.title}")
    return redirect('job_listing')

@login_required
def my_applications(request):
    # Get the jobs that the applicant has applied to
    applied_jobs = JobApplication.objects.filter(applicant=request.user)

    # Render the template and pass the list of jobs
    return render(request, 'job/my_applications.html', {'applied_jobs': applied_jobs})


@login_required
def view_applicants(request, job_id):
    # Get the job object based on job_id
    job = get_object_or_404(Job, id=job_id)

    if job.user != request.user: # Ensure that only the recruiter who posted the job can view the applicants
        messages.error(request, "You are not authorized to view applicants for this job.")
        return redirect('home')

   
    applicants = JobApplication.objects.filter(job=job)# Get all the job applications for this job

    return render(request, 'job/view_applicants.html', {'job': job, 'applicants': applicants})
