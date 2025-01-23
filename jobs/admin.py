from django.contrib import admin

# Register your models here.

from .models import JobPost,Graph,GraphDescription

admin.site.register(JobPost)
admin.site.register(Graph)
admin.site.register(GraphDescription)
