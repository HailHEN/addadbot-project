from django.contrib import admin

# Register your models here.
admin.site.index_template = 'admin-custom-function.html'
from .models import JobPost
admin.site.register(JobPost)
