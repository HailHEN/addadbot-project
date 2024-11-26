
from jobs.models import JobPost
from jobs.management.commands._data_analysis import JobPostingsAnalysis
from django.core.management.base import BaseCommand





class Command(BaseCommand):

     def handle(self, *args, **options):
          d_analysis = JobPostingsAnalysis(JobPost.objects.all().values())
          self.stdout.write(d_analysis.data_frame().to_string())
          

          #user selects what to graph

          #demo

          d_analysis.analyse_postings_date_created()


          
          self.stdout.write(self.style.SUCCESS('Successfully ran analysis!'))
          return