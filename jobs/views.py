from django.shortcuts import render
from plotly import express as px

from django.http import HttpResponse
from jobs.models import JobPost
from analyse_postings.data_analysis import JobPostingsAnalysis
from matplotlib import pyplot as plt
import pandas as pd

def charts_setup(df, list_of_skills_unique, frequency_of_skills_counts):

    fig = px.line(df, x='date_posted', title="Total jobs posted", markers=True, color='job_country')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    fig.update_layout(title_x=0.5,yaxis=dict(tickmode = 'linear',
        tick0 = 0,
        dtick = 1))



    chart = fig.to_html()



    
    

    fig = px.bar(df, x="area_of_expertise",
                 width=325, height=225)
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
                 width=325, height=225)
    fig.update_layout(title_text='Domain of robotics', title_x=0.5)
    chart6 = fig.to_html()

    #so later, maybe use line graphs with date as x axis (can be acheived by using color as skills and x axis date)
    fig = px.bar(x=list_of_skills_unique, y=frequency_of_skills_counts, width=650, height=450,
                 )
    fig.update_layout(title_text='Skills in robotics', title_x=0.5,
                       xaxis_title="Skills", yaxis_title="count")
    chart7 = fig.to_html()

    fig = px.pie(df,values='job_count', names='job_country', title="Jobs posted per country"
                 ,width=650, height=450, labels={'job_count':'Jobs','job_country':'Country'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    chart8 = fig.to_html()

    return {'chart': chart, 'chart3': chart3, 'chart4': chart4,
               'chart5': chart5, 'chart6': chart6, 'chart7':chart7, 'chart8':chart8}


def viewStats(request):

    d_analysis = JobPostingsAnalysis(JobPost.objects.all().values())
    # print(d_analysis.data_frame().to_string())

    df = d_analysis.get_data_frame()
    

    list_of_skills_unique, frequency_of_skills_counts  = d_analysis.keywords_skill_description_analyser()

    

    # df['Skills'].value_counts().plot(kind='bar')

    # filter here will be the scale of x axis
    # fig = px.histogram(df, x="date_posted",
    #                    title="Total jobs posted",width=650, height=450)
    # fig.update_layout(title_text='Total jobs posted', title_x=0.5)

    df['job_count'] = pd.Series([1 for x in range(len(df.index))])

    context = charts_setup(df, list_of_skills_unique, frequency_of_skills_counts)
    

    posted_dictionary, job_position_list = d_analysis.stats_summary_for_jobs_posted()

    context['job_posted_stat_summary_list'] = posted_dictionary
    context['job_posted_stat_summary_list_inc_type'] = job_position_list

    # exp_dict = d_analysis.area_of_expertise_stat_summary()
    
    # context['expertise_posted']
    

    return render(request, "jobs/stats.html", context )

    


# Create your views here.
