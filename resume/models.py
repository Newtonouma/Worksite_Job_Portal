from django.db import models
from django.contrib.auth.models import User  # Import User from django.contrib.auth

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    second_name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    # You can add a field for uploading a CV, for example:
    cv = models.FileField(upload_to='resumes/', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


