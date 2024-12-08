from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Company
from django.contrib.auth.models import User  # Import the default User model
from .forms import UpdateCompanyForm  # Ensure correct file naming convention


def update_company(request):
    # Fetch the company associated with the current user
    company = get_object_or_404(Company, user=request.user)
    
    if request.method == 'POST':
        form = UpdateCompanyForm(request.POST, instance=company)
        if form.is_valid():
            # Save the company form and update the user model
            form.save()
            request.user.has_company = True
            request.user.save()
            messages.info(request, 'Your company is active, make some job boards')
            return redirect('dashboard')  # Corrected redirect
        else:
            messages.warning(request, 'Something went wrong')
    else:
        form = UpdateCompanyForm(instance=company)
    
    context = {'form': form}
    return render(request, 'company/update_company.html', context)


def company_details(request, pk):
    # Fetch the company instance using get_object_or_404 for better error handling
    company = get_object_or_404(Company, pk=pk)
    context = {'company': company}
    return render(request, 'company_details.html', context)  # Corrected render usage

