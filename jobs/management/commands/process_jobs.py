from django.core.management.base import BaseCommand, CommandError
from jobs.models import JobPost
import plotly
from plotly import express as px


from analyse_postings.data_analysis import JobPostingsAnalysis
from analyse_postings.setup_graphs import ChartSetups
import pandas as pd



class Command(BaseCommand):
    

    

    def handle(self, *args, **options):
            d_analysis = JobPostingsAnalysis(JobPost.objects.all().values())
            count_of_jobs = JobPost.objects.all().count()
            df = d_analysis.get_data_frame()
            list_of_skills_unique, frequency_of_skills_counts  = d_analysis.keywords_skill_description_analyser()
            df['job_count'] = pd.Series([1 for x in range(len(df.index))])
            ChartSetups.charts_setup(df, list_of_skills_unique, frequency_of_skills_counts)
        

            self.stdout.write(
                self.style.SUCCESS('Successfully created graph page.')
            )

