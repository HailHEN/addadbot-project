from django.shortcuts import render
from plotly import express as px

from django.http import HttpResponse
from jobs.models import JobPost
from analyse_postings.data_analysis import JobPostingsAnalysis


def viewStats(request):

    d_analysis = JobPostingsAnalysis(JobPost.objects.all().values())
    print(d_analysis.data_frame().to_string())

    df = JobPostingsAnalysis(JobPost.objects.all().values()).get_data_frame()

    
    fig = px.histogram(df, x="date_posted")
    chart = fig.to_html()
    context = {'chart': chart}
    
    


    
    if request.method == "GET":
        chartselection = request.GET.get('graphs')

        if chartselection == "post":
            fig = px.histogram(df, x="date_posted", title="Job Postings")
            chart = fig.to_html()
            context = {'chart': chart}
            return render(request, "jobs/stats.html", context)

        
        if chartselection == "robot-type":
            fig = px.bar(df, x="robot_type", title="Job Postings based on robot types")
            chart = fig.to_html()
            context = {'chart': chart}
            print("yes")
            return render(request, "jobs/stats.html", context)

        if chartselection == "expertise":
            fig = px.bar(df, x="area_of_expertise")
            chart = fig.to_html()
            context = {'chart': chart}
            return render(request, "jobs/stats.html", context)

        # we will need a skills analyser for the job description secrtion
        if chartselection == "skills":
            fig = px.bar(df, x="robot_type")
            chart = fig.to_html()
            context = {'chart': chart}
            return render(request, "jobs/stats.html", context)
        

        
        if chartselection == "position":
            fig = px.bar(df, x="job_position")
            chart = fig.to_html()
            context = {'chart': chart}
            return render(request, "jobs/stats.html", context)
        
        # context['numberJobList'] = 
    

    

    return render(request, "jobs/stats.html", context )

    


# Create your views here.
