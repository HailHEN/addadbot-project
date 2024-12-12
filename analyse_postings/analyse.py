
from jobs.models import JobPost
from data_analysis import JobPostingsAnalysis
from django.core.management.base import BaseCommand





class Command(BaseCommand):

     def handle(self, *args, **options):
          d_analysis = JobPostingsAnalysis(JobPost.objects.all().values())
          print(d_analysis.data_frame().to_string())
          
          

          #user selects what to graph

          #demo

          d_analysis.analyse_type_of_robotics()


          
          self.stdout.write(self.style.SUCCESS('Successfully ran analysis!'))
          
          return