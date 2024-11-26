
from jobs.models import JobPost
from jobs.management.commands._data_analysis import JobPostingsAnalysis
from django.core.management.base import BaseCommand, CommandError





class Command(BaseCommand):

     def handle(self, *args, **options):
          d_analysis = JobPostingsAnalysis(JobPost.objects.all())
          
          self.stdout.write(self.style.SUCCESS('Successfully ran analysis!'))
          return