
from datetime import date


class JobPosts:
    # employment type is part time or full time etc
    # position is: intern position, junior, senior etc
    # position title is if is an engineering or software etc role 
    # domain is if it is in medical, space etc


    def __init__(self, job_title, date_posted, job_country, job_position, position_title, employment_type, robot_type, robotics_domain):
        self.job_title = job_title
        self.date_posted = date(date_posted)
        self.job_country = job_country
        self.job_position = job_position
        self.position_title = position_title
        self.employment_type = employment_type
        self.robot_type = robot_type
        self.robotics_domain = robotics_domain
