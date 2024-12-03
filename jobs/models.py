from django.db import models

# Create your models here.


# employment type is part time or full time etc
# position is: intern position, junior, senior etc
# position title is if is an engineering or software etc role 
# domain is if it is in medical, space etc


class JobPost(models.Model):
    job_title = models.CharField(max_length=200)
    date_posted = models.DateField()

    job_country = models.CharField(max_length=200)
    # position type (includes position_title) 
    job_position = models.CharField(max_length=200)

    # add area of expertise include (control, machine learning, deep learnign, perception, motion planning, path plannnign etc...)

    # position_title = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=200)
    robot_type = models.CharField(max_length=200)
    robotics_domain = models.CharField(max_length=200)   


# JobPost(job_title = "Robotics at NASA", date_posted = date.today(),
#         job_country = "Australia", job_position = "Junior",
#         position_title = "Software Developer",
#         employment_type = "Full time",
#         robot_type = "Vehicle",
#         robotics_domain = "Aerospace")