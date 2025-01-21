from django.shortcuts import render
from plotly import express as px

from django.http import HttpResponse
from jobs.models import JobPost

from analyse_postings.data_analysis import JobPostingsAnalysis
from matplotlib import pyplot as plt
import pandas as pd

def charts_setup(df, list_of_skills_unique, frequency_of_skills_counts):
    count_of_jobs = JobPost.objects.all().count()
    
    line_df = df[["date_posted", "job_country"]]
    temp_line_df = line_df
    line_df = pd.DataFrame(line_df['date_posted'].dt.date.value_counts()).reset_index()
    line_df['date_posted'] = pd.to_datetime(line_df['date_posted'])
    line_df = temp_line_df.merge(line_df, how='left', on='date_posted')
    

    fig = px.line(line_df, x='date_posted', y = 'count', title="Total jobs posted", markers=True, color='job_country')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    fig.update_layout(margin=dict(
        l=0,
        r=0,
        b=80,
        t=40,
        pad=4), title_x=0.5,yaxis=dict(tickmode = 'linear',
        tick0 = 0,
        dtick = 1))



    chart = fig.to_html()



    
    

    fig = px.bar(df, x="area_of_expertise",
                 width=600, height=450)
    fig.update_layout(xaxis={'categoryorder':'total descending'}) 
    fig.update_layout(margin=dict(
        l=0,
        r=0,
        b=10,
        t=40,
        pad=4),title_text='Area of expertise', title_x=0.5)
    chart3 = fig.to_html()
    
    fig = px.bar(df, x="employment_type",
                 width=650, height=450)
    
    fig.update_layout(margin=dict(
        l=0,
        r=0,
        b=10,
        t=40,
        pad=4),title_text='Type of employment posted', title_x=0.5)
    fig.update_layout(xaxis={'categoryorder':'total descending'}) 
    chart4 = fig.to_html()

    fig = px.bar(df, x="robot_type",
                 width=650, height=450)
    fig.update_layout(margin=dict(
        l=0,
        r=0,
        b=10,
        t=40,
        pad=4),title_text='Types of robots used by employers', title_x=0.5)
    fig.update_layout(xaxis={'categoryorder':'total descending'}) 
    chart5 = fig.to_html()

    fig = px.bar(df, x="robotics_domain",
                 width=600, height=450)
    fig.update_layout(margin=dict(
        l=0,
        r=0,
        b=10,
        t=40,
        pad=4),title_text='Domain of robotics', title_x=0.5)
    fig.update_layout(xaxis={'categoryorder':'total descending'}) 
    chart6 = fig.to_html()

    #so later, maybe use line graphs with date as x axis (can be acheived by using color as skills and x axis date)
    fig = px.bar(x=list_of_skills_unique, y=frequency_of_skills_counts, width=650, height=450,
                 )
    fig.update_layout(margin=dict(
        l=0,
        r=0,
        b=10,
        t=40,
        pad=4),title_text='Skills in robotics', title_x=0.5,
                       xaxis_title="Skills", yaxis_title="count")
    
    fig.update_layout(xaxis={'categoryorder':'total descending'}) 
    chart7 = fig.to_html()

    fig = px.pie(df,values='job_count', names='job_country', title="Jobs posted per country"
                 ,width=650, height=450, labels={'job_count':'Jobs','job_country':'Country'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    chart8 = fig.to_html()

    fig = px.sunburst(df, path=['employment_type', 'job_position', 'robot_type'], values='job_count', color='employment_type')
    chart9 = fig.to_html()


    return {'chart': chart, 'chart3': chart3, 'chart4': chart4,
               'chart5': chart5, 'chart6': chart6, 'chart7':chart7, 'chart8':chart8, 'chart9':chart9, 'count_of_jobs':count_of_jobs}


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
    exp_list = d_analysis.area_of_expertise_stat_summary()
    context['domain_expertise_list'] = exp_list
    context['robot_type_dict'] = d_analysis.types_of_robot_stat_summary()
     
    
    # context['expertise_posted']
    

    return render(request, "jobs/stats.html", context )

    


# Create your views here.
