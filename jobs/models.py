from django.db import models

# Create your models here.

class JobPost(models.Model):

    def clean_skills(self):
        self.required_skills
        return
    job_title = models.CharField(max_length=200)
    date_posted = models.DateField()

    job_country = models.CharField(max_length=200)
    # position type (includes position_title) 
    job_position = models.CharField(max_length=200)

    # add area of expertise include (control, machine learning, deep learnign, perception, motion planning, path plannnign etc...)
    area_of_expertise = models.CharField(max_length=200)

    # position_title = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=200)
    robot_type = models.CharField(max_length=200)
    robotics_domain = models.CharField(max_length=200)  
    job_description = models.TextField(max_length=2000)
    required_skills = models.TextField(max_length=1000)
    



