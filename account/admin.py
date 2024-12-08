from django.contrib import admin
from resume.models import Resume
from company.models import Company

# Register the model
admin.site.register(Resume)
admin.site.register(Company)


