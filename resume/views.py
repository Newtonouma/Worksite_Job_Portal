from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import UpdateResumeForm
from .models import Resume
from django.contrib.auth.models import User

@login_required
def update_resume(request):
    try:
        # Get the current user's resume
        resume = Resume.objects.get(user=request.user)
    except Resume.DoesNotExist:
        # Handle the case where the resume does not exist
        messages.warning(request, "No resume found for this user.")
        return redirect('dashboard')  # Redirect to dashboard or any other page
    
    if request.method == 'POST':
        form = UpdateResumeForm(request.POST, instance=resume)
        if form.is_valid():
            var = form.save(commit=False)
            user = request.user
            user.has_resume = True
            user.save()
            var.save()
            messages.info(request, 'Your Resume Has been updated')
            return redirect('dashboard')  # Redirect after successful update
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = UpdateResumeForm(instance=resume)
    
    # Use render instead of redirect to display the form
    context = {'form': form}
    return render(request, 'resume/update_resume.html', context)

    
def resume_details(request, pk):
    resume = Resume.objects.get(pk=pk)
    context = {'resume':resume}
    return render(request, 'resume/update_details.html')


# Create your views here.
