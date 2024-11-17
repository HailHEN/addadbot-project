from django.db import models

# Create your models here.
class JobPost(models.Model):
    job_title = models.CharField(max_length=200)
    date_posted = models.DateTimeField()
    job_country = models.CharField(max_length=200)
    job_position = models.CharField(max_length=200)
    position_title = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=200)
    robot_type = models.CharField(max_length=200)
    robotics_domain = models.CharField(max_length=200)