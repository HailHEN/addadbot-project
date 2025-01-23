from django.core.management.base import BaseCommand, CommandError
from jobs.models import JobPost
from jobs.models import Graph, GraphDescription
import plotly
from plotly import express as px
import json


from analyse_postings.data_analysis import JobPostingsAnalysis
from analyse_postings.setup_graphs import ChartSetups
import pandas as pd
import os



class Command(BaseCommand):
    

    

    def handle(self, *args, **options):
            d_analysis = JobPostingsAnalysis(JobPost.objects.all().values())
            count_of_jobs = JobPost.objects.all().count()
            df = d_analysis.get_data_frame()
            list_of_skills_unique, frequency_of_skills_counts  = d_analysis.keywords_skill_description_analyser()
            context = dict()

            df['job_count'] = pd.Series([1 for x in range(len(df.index))])
            ChartSetups.charts_setup(df, list_of_skills_unique, frequency_of_skills_counts)
            self.stdout.write(
                self.style.SUCCESS('Graphs constructed.')
            )

            context['count_of_jobs'] = count_of_jobs
            # next process all the files from the graphs folder (so iterate over the graphs folder and then map it to this dictionary)
            posted_dictionary, job_position_list = d_analysis.stats_summary_for_jobs_posted()

            context['job_posted_stat_summary_list'] = posted_dictionary
            context['job_posted_stat_summary_list_inc_type'] = job_position_list
            exp_list = d_analysis.area_of_expertise_stat_summary()
            context['domain_expertise_list'] = exp_list
            context['robot_type_dict'] = d_analysis.types_of_robot_stat_summary()

            
            self.stdout.write(
                self.style.SUCCESS('Saving descriptions.')
            )
            GraphDescription.objects.all().delete()
            descriptions = GraphDescription(description_dictionary = json.dumps(context))
            descriptions.save()
            self.stdout.write(
                self.style.SUCCESS('Descriptions saved.')
            )

            

        

            
