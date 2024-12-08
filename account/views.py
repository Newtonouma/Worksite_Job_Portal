from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Item
from resume.models import Resume
from company.models import Company
from django.contrib.auth.models import Group


# registration of applicants only

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password != password_confirmation:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            # Create the user
            user = User.objects.create_user(username=username, password=password)
            
            # Assign the user to the "Applicant" group
            applicant_group, created = Group.objects.get_or_create(name='Applicant')
            user.groups.add(applicant_group)
            user.save()

            # Create a resume linked to the user
            Resume.objects.create(user=user)

            # Display success message and redirect to login
            messages.success(request, 'Account created successfully')
            return redirect('login')

    return render(request, 'register.html')

# regester as a recruiter

def register_recruiter(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if password != password_confirmation:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register_recruiter.html')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            # Create user
            user = User.objects.create_user(username=username, password=password)
            
            # Assign the user to the "Recruiter" group
            recruiter_group, created = Group.objects.get_or_create(name='Recruiter')
            user.groups.add(recruiter_group)
            user.save()

            # Create a company profile linked to the recruiter user
            Company.objects.create(user=user)

            # Display success message and redirect
            messages.success(request, 'Account created successfully')
            return redirect('login')

    return render(request, 'register_recruiter.html')



# Login User

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')
    

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
