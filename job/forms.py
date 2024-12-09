from django import forms
from .models import Job, JobApplication


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job  
        exclude = ('user', 'company')

class UpdateJobForm(forms.ModelForm):
    class meta:
        model = Job
        exclude = ('user', 'company')

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'location', 'salary', 'requirement', 'ideal_candidate', 'is_available']
        widgets = {
            'requirement': forms.Textarea(attrs={'rows': 3}),
            'ideal_candidate': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'is_available': 'Is the job currently available?',
        }


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []  # Since we are not accepting any additional input, no fields are needed
