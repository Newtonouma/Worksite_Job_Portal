from django.contrib import admin
from resume.models import Resume
from company.models import Company
from job.models import Job, JobApplication


# Register the model
admin.site.register(Resume)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(JobApplication)


