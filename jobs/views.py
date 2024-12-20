from django.shortcuts import render
from plotly import express as px

from django.http import HttpResponse
from jobs.models import JobPost
from analyse_postings.data_analysis import JobPostingsAnalysis
from matplotlib import pyplot as plt


def viewStats(request):

    d_analysis = JobPostingsAnalysis(JobPost.objects.all().values())
    # print(d_analysis.data_frame().to_string())

    df = d_analysis.get_data_frame()

    list_of_skills_unique, frequency_of_skills_counts  = d_analysis.keywords_skill_description_analyser()

    

    # df['Skills'].value_counts().plot(kind='bar')

    # filter here will be the scale of x axis
    fig = px.histogram(df, x="date_posted",
                       title="Total jobs posted",width=650, height=450)
    fig.update_layout(title_text='Total jobs posted', title_x=0.5)
    chart = fig.to_html()
    
    fig = px.bar(df, x="robot_type", title="Job Postings based on robot types"
                 ,width=650, height=450)
    fig.update_layout(title_text='Job Postings based on robot types', title_x=0.5)
    chart2 = fig.to_html()

    fig = px.bar(df, x="area_of_expertise",
                 width=650, height=450)
    fig.update_layout(title_text='Area of expertise', title_x=0.5)
    chart3 = fig.to_html()
    

    fig = px.bar(df, x="employment_type",
                 width=650, height=450)
    fig.update_layout(title_text='Type of employment posted', title_x=0.5)
    chart4 = fig.to_html()

    fig = px.bar(df, x="robot_type",
                 width=650, height=450)
    fig.update_layout(title_text='Types of robots used by employers', title_x=0.5)
    chart5 = fig.to_html()


    fig = px.bar(df, x="robotics_domain",
                 width=650, height=450)
    fig.update_layout(title_text='Domain of robotics', title_x=0.5)
    chart6 = fig.to_html()


    #so later, maybe use line graphs with date as x axis (can be acheived by using color as skills and x axis date)
    fig = px.bar(x=list_of_skills_unique, y=frequency_of_skills_counts, width=650, height=450,
                 )
    fig.update_layout(title_text='Skills in robotics', title_x=0.5,
                       xaxis_title="Skills", yaxis_title="count")
    chart7 = fig.to_html()

    

    

    context = {'chart': chart, 'chart2': chart2, 'chart3': chart3, 'chart4': chart4,
               'chart5': chart5, 'chart6': chart6, 'chart7':chart7}
        
        
    

    

    return render(request, "jobs/stats.html", context )

    


# Create your views here.
